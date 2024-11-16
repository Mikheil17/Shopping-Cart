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
        # returns all orders from a user, may be done 
        self.cursor.execute("SELECT * FROM Orders WHERE userID = ?", (userID))
        return self.cursor.fetchall()
    
    def viewOrder(self, userID, orderID):
        # returns the OrderItems rows, connect with cart, finish after createOrder and addOrderItems
        self.cursor.execute("SELECT cost, date FROM Orders WHERE userID = ? AND orderID = ?", (userID, orderID))
        return self.cursor.fetchall()
    
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
    
    def addOrderItems(self, userID, orderID):
        pass
    
    def close(self):
        # Close the database connection.
        self.connection.close()    
