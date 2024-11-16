import sqlite3

class Inventory:
    def __init__(self, database_name="methods.db"):

        self.database_name = database_name
        self.connection = sqlite3.connect(self.database_name)
        self.cursor = self.connection.cursor()

    def viewInventory(self):
            query = "SELECT * FROM Inventory"
            self.cursor.execute(query)
            return self.cursor.fetchall()

    def searchInventory(self, Title):

        query = "SELECT * FROM Inventory WHERE Title LIKE ?"
        self.cursor.execute(query, ('%' + Title + '%',))  # Use LIKE for partial matches
        results = self.cursor.fetchall()

        if results:
            return results
        else:
            print(f"No inventory items found for title: {Title}")
            return []

    def decreaseStock(self, ISBN, Quantity=1):

        query = "UPDATE inventory SET Stock = Stock - ? WHERE ISBN = ?"
        self.cursor.execute(query, (Quantity, ISBN))
        self.connection.commit()

    def close(self):
    
        self.connection.close()
