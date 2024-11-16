import sqlite3

class Inventory:

    def __init__(self, database_name="methods.db"):
        # Initialize the Inventory class with a database connection.
        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def viewInventory(self, userID=None):
        # If a userID is passed, fetch inventory for that user
        if userID:
            query = "SELECT * FROM inventory WHERE userID = ?"
            self.cursor.execute(query, (userID,))
        else:
            query = "SELECT * FROM inventory"
            self.cursor.execute(query)

        # Fetch all inventory rows
        return self.cursor.fetchall()


    
    def addToInventory(self, userID, ISBN, title, author, genre, pages, quantity, cost):
        # Insert a new item into the inventory
        query = "INSERT INTO inventory (userID, ISBN, title, author, genre, pages, quantity, cost) VALUES (?, ?, ?, ?, ?, ?, ?, ?)"
        self.cursor.execute(query, (userID, ISBN, title, author, genre, pages, quantity, cost))
        self.connection.commit()  # Commit the transaction to save changes

    def updateInventory(self, userID, ISBN, cost, Quantity=None):
        # Prepare the query and parameters
        if Quantity is not None:
            query = "UPDATE inventory SET Quantity = ?, cost = ? WHERE userID = ? AND ISBN = ?"
            self.cursor.execute(query, (Quantity, cost, userID, ISBN))
        else:
            query = "UPDATE inventory SET cost = ? WHERE userID = ? AND ISBN = ?"
            self.cursor.execute(query, (cost, userID, ISBN))

        self.connection.commit()

    def removeFromInventory(self, userID, ISBN):
        query = "DELETE FROM inventory WHERE userID = ? AND ISBN = ?"
        self.cursor.execute(query, (userID, ISBN))
        self.connection.commit()

    def close(self):
        # Close the database connection.
        self.connection.close()
