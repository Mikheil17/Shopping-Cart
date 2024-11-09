import sqlite3

class Inventory:

    def __init__(self, database_name="methods.db"):
        
        #Initialize the Inventory class with a database connection.
        self.database_name = database_name
    
    def viewInventory(self):
        pass
        # Retrieve all items in the inventory, optionally filtered by genre.
        
        
    def addToInventory(self, UserID, ISBN, Quantity, cost):
        pass # Insert a new item into the inventory
    def updateItem(self, userID, ISBN, Quantity = none, cost):
        pass # Update any items
    def removeItem(self, userID, ISBN):
        pass # Remove any items

    def close(self):
        # Close the database connection.
        self.connection.close()
