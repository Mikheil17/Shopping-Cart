import sqlite3

class Inventory:

    def __init__(self, database_name="methods.db"):
        # Initialize the Inventory class with a database connection.
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)  # Establish connection
        self.cursor = self.connection.cursor()  # Create a cursor to interact with the DB
    
    def viewInventory(self, userID=None):
        # Query for all inventory or inventory for a specific user if userID is provided
        if userID:
            query = "SELECT * FROM inventory WHERE userID = ?"
            self.cursor.execute(query, (userID,))
        else:
            query = "SELECT * FROM inventory"
            self.cursor.execute(query)
        
        # Fetch and return all the rows in the result
        rows = self.cursor.fetchall()
        return rows
        
    def addToInventory(self, userID, ISBN, quantity, cost):
        # Insert a new item into the inventory
        query = "INSERT INTO inventory (userID, ISBN, Quantity, cost) VALUES (?, ?, ?, ?)"
        self.cursor.execute(query, (userID, ISBN, quantity, cost))
        self.connection.commit()  # Commit the transaction to save changes
        
    def updateInventory(self, userID, ISBN, cost, quantity=None):
        # Update the inventory for a specific user and ISBN
        if quantity is not None:
            query = "UPDATE inventory SET Quantity = ?, cost = ? WHERE userID = ? AND ISBN = ?"
            self.cursor.execute(query, (quantity, cost, userID, ISBN))
        else:
            query = "UPDATE inventory SET cost = ? WHERE userID = ? AND ISBN = ?"
            self.cursor.execute(query, (cost, userID, ISBN))
        
        self.connection.commit()  # Commit the transaction to save changes
        
    def removeFromInventory(self, userID, ISBN):
        # Remove an item from the inventory for a specific user and ISBN
        query = "DELETE FROM inventory WHERE userID = ? AND ISBN = ?"
        self.cursor.execute(query, (userID, ISBN))
        self.connection.commit()  # Commit the transaction to save changes

    def close(self):
        # Close the database connection.
        self.connection.close()
