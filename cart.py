import sqlite3
import datetime
from inventory import Inventory
from history import OrderHistory

class Cart:

    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName
        self.connection = sqlite3.connect(self.databaseName)
        self.cursor = self.connection.cursor()
        self.createTable()

    def createTable(self):
        # Creates the cart table if it doesn't exist
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS cart (
                userID TEXT,
                ISBN TEXT,
                quantity INTEGER,
                PRIMARY KEY (userID, ISBN)
            )
        """)
        self.connection.commit()

    def viewCart(self, userID):
        # Display all books in the user's cart
        self.cursor.execute("SELECT ISBN, quantity FROM cart WHERE userID = ?", (userID,))
        cart_items = self.cursor.fetchall()

        if cart_items:
            print(f"Cart for User ID {userID}:")
            for ISBN, quantity in cart_items:
                print(f"ISBN: {ISBN}, Quantity: {quantity}")
        else:
            print(f"Your cart is empty, User ID {userID}.")

    def addToCart(self, userID, ISBN, quantity=1):
        # Check if the item already exists in the cart
        self.cursor.execute("SELECT quantity FROM cart WHERE userID = ? AND ISBN = ?", (userID, ISBN))
        existing_item = self.cursor.fetchone()

        if existing_item:
            # If the item exists, update its quantity
            self.cursor.execute("""
                UPDATE cart SET quantity = quantity + ?
                WHERE userID = ? AND ISBN = ?
            """, (quantity, userID, ISBN))
            print(f"Updated quantity of ISBN {ISBN} in the cart.")
        else:
            # If the item does not exist, insert it
            self.cursor.execute("""
                INSERT INTO cart (userID, ISBN, quantity)
                VALUES (?, ?, ?)
            """, (userID, ISBN, quantity))
            print(f"Added ISBN {ISBN} to the cart.")
        self.connection.commit()
    
    def removeFromCart(self, userID, ISBN):
        # Remove an item from the user's cart
        self.cursor.execute("DELETE FROM cart WHERE userID = ? AND ISBN = ?", (userID, ISBN))
        self.connection.commit()
        print(f"Removed ISBN {ISBN} from the cart.")

    def checkOut(self, userID):
        # Get the current date
        current_date = datetime.date.today().isoformat()  # Format as 'YYYY-MM-DD'

        # Process the checkout
        inventory = Inventory(self.databaseName)
        history = OrderHistory(self.databaseName)

        # Fetch cart items
        self.cursor.execute("SELECT ISBN, quantity FROM cart WHERE userID = ?", (userID,))
        cart_items = self.cursor.fetchall()

        if not cart_items:
            print(f"No items in the cart for User ID {userID}. Checkout cannot proceed.")
            return

        print("Processing checkout...")

        # Initialize total cost
        total_cost = 0

        # Check inventory and update total cost
        for ISBN, quantity in cart_items:
            # Get cost per item from the inventory
            inventory.cursor.execute("SELECT cost, Quantity FROM inventory WHERE ISBN = ?", (ISBN,))
            inventory_data = inventory.cursor.fetchone()

            if not inventory_data:
                print(f"Error: ISBN {ISBN} not found in inventory. Checkout aborted.")
                return

            cost, available_stock = inventory_data

            if available_stock < quantity:
                print(f"Error: Insufficient stock for ISBN {ISBN}. Checkout aborted.")
                return

            # Update the total cost
            total_cost += cost * quantity

            # Decrease stock in the inventory
            inventory.decreaseStock(None, ISBN, quantity)

        # Create an order and get the generated orderID
        orderID = history.createOrder(userID, len(cart_items), total_cost, current_date)

        # Add items from the cart to the OrderItems table
        history.addOrderItems(userID, orderID)

        # Finalize the order cost in the Orders table
        self.cursor.execute("UPDATE Orders SET cost = ? WHERE orderID = ?", (total_cost, orderID))
        self.connection.commit()

        # Clear the user's cart
        self.cursor.execute("DELETE FROM cart WHERE userID = ?", (userID,))
        self.connection.commit()

        print(f"Checkout complete! Your cart has been cleared and order {orderID} has been created.")

    def close(self):
        # Close the database connection.
        self.connection.close()    