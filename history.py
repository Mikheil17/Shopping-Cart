import sqlite3
import random
from inventory import Inventory

class OrderHistory:

    def __init__(self, databaseName="methods.db"):
        self.databaseName = databaseName
        self.connection = sqlite3.connect(self.databaseName)
        self.cursor = self.connection.cursor()
        self.createHistory()
    
    def createHistory(self):
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS Orders (
                orderID TEXT,
                userID TEXT,
                itemNumber TEXT,
                cost FLOAT,
                date TEXT,
                PRIMARY KEY (orderID),
                FOREIGN KEY (userID)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS OrderItems (
                orderID TEXT,
                ISBN TEXT,
                quantity INTEGER,
                FOREIGN KEY (orderID, ISBN)
            )
        """)
        self.connection.commit()
    
    def viewHistory(self, userID):
        self.cursor.execute("SELECT * FROM Orders WHERE userID = ?", (userID))
        history = self.cursor.fetchall()
        if history:
            print(f"Orders for User ID {userID}:")
            for orderID, cost, date in history:
                print(f"OrderID: {orderID}, Cost: {cost}, Date: {date}")
        else:
            print(f"You have no orders, User ID {userID}.")
    
    def viewOrder(self, userID, orderID):
        self.cursor.execute("SELECT userID FROM Orders WHERE orderID = ?", (orderID))
        confirmOrder = self.cursor.fetchone()
        if confirmOrder != userID:
            print("Unable to view. Your userID does not match the order you are trying to access.")
            return
        self.cursor.execute("SELECT ISBN, quantity FROM OrderItems WHERE orderID = ?", (orderID))
        fullOrder = self.cursor.fetchall()
        print("Ordered items: ")
        for ISBN in fullOrder:
            self.cursor.execute("SELECT Title, Author FROM Inventory WHERE ISBN = ?", (ISBN))
            currentItem = self.cursor.fetchall()
            print(f"{Title} by {Author}, Quantity: {quantity} \n")
    
    def createOrder(self, userID, itemNumber, cost, date):
        orderID = random.randint()
        taken = self.viewOrder(userID, orderID)
        while taken:
            orderID = random.randint()
            taken = self.viewOrder(userID, orderID)
        self.cursor.execute("""
                INSERT INTO Orders (orderID, userID, itemNumber, cost, date)
                VALUES (?, ?, ?, ?, ?)
            """, (orderID, userID, itemNumber, cost, date))
        self.connection.commit()
        return str(orderID)
    
    def addOrderItems(self, userID, orderID):
        self.cursor.execute("SELECT * FROM cart WHERE userID = ?", (userID))
        items = self.cursor.fetchall()
        for item in items:
            self.cursor.execute("""
                INSERT INTO OrderItems (orderID, ISBN, quantity)
                VALUES (?, ?, ?)
            """, (orderID, ISBN, quantity))
            self.connection.commit()
    
    def close(self):
        # Close the database connection.
        self.connection.close()    
