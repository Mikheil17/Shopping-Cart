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
                OrderNumber varchar(6) NOT NULL,
                UserID varchar(7) NOT NULL,
                ItemNumber int(5),
                Cost varchar(10),
                Date varchar(25),
                PRIMARY KEY(OrderNumber),
                FOREIGN KEY(UserID) REFERENCES User(UserID)
            )
        """)
        self.cursor.execute("""
            CREATE TABLE IF NOT EXISTS OrderItems (
                OrderNumber varchar(6) NOT NULL,
                ISBN varchar(14) NOT NULL,
                Quantity int(3),
                FOREIGN KEY(OrderNumber) REFERENCES Orders(OrderNumber),
                FOREIGN KEY(ISBN) REFERENCES Inventory(ISBN)
            )
        """)
        self.connection.commit()
    
    def viewHistory(self, userID):
        self.cursor.execute("SELECT * FROM Orders WHERE UserID = ?", (userID))
        history = self.cursor.fetchall()
        if history:
            print(f"Orders for User ID {userID}:")
            for orderID, cost, date in history:
                print(f"OrderNumber: {orderID}, Cost: {cost}, Date: {date}")
        else:
            print(f"You have no orders, User ID {userID}.")
    
    def viewOrder(self, userID, orderID):
        self.cursor.execute("SELECT UserID FROM Orders WHERE OrderNumber = ?", (orderID))
        confirmOrder = self.cursor.fetchone()
        if not confirmOrder:
            print("The order you are looking for could not be found. Please try again.")
            break
            
        if confirmOrder != userID:
            print("Unable to view. Your userID does not match the order you are trying to access.")
            return
        self.cursor.execute("SELECT ISBN, quantity FROM OrderItems WHERE OrderNumber = ?", (orderID))
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
                INSERT INTO Orders (OrderNumber, UserID, ItemNumber, Cost, Date)
                VALUES (?, ?, ?, ?, ?)
            """, (orderID, userID, itemNumber, cost, date))
        self.connection.commit()
        return str(orderID)
    
    def addOrderItems(self, userID, orderID):
        self.cursor.execute("SELECT * FROM cart WHERE userID = ?", (userID))
        items = self.cursor.fetchall()
        for item in items:
            self.cursor.execute("""
                INSERT INTO OrderItems (OrderNumber, ISBN, quantity)
                VALUES (?, ?, ?)
            """, (orderID, ISBN, quantity))
            self.connection.commit()
    
    def close(self):
        # Close the database connection.
        self.connection.close()    
