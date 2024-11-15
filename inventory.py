import sqlite3

class Inventory:

    def __init__(self, database_name="methods.db"):
        
        #Initialize the Inventory class with a database connection.
        self.database_name = database_name
    
    def viewInventory(self):
        if userID:
            query = "SELECT * FROM inventory WHERE userID = ?"
            self.cursor.execute(query, (userID,))
        else:
            query = "SELECT * FROM inventory"
            self.cursor.execute(query)
        
        # Fetch and return all the rows in the result
        rows = self.cursor.fetchall()
        return rows
        
    def addToInventory(self, UserID, ISBN, Quantity, cost):
        pass # Insert a new item into the inventory
        
    def updateInventory(self, userID, ISBN, cost, Quantity = none):
        pass # Update any items
    def removeFromInventory(self, userID, ISBN):
        pass # Remove any items

    def close(self):
        # Close the database connection.
        self.connection.close()
