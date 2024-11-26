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
        query = "SELECT ISBN, Title, Author, Genre, Pages, ReleaseDate, Price, Stock FROM Inventory WHERE Title LIKE ?"
        self.cursor.execute(query, ('%' + Title + '%',))  # Use LIKE for partial matches
        results = self.cursor.fetchall()

        if results:
            print(f"\nSearch Results:")
            print(f"{'ISBN':<20} {'Title':<50} {'Author':<30} {'Genre':<25} {'Pages':<8} {'ReleaseDate':<12} {'Price':<8} {'Stock':<8}")
            print("-" * 150)
            for item in results:
                print(f"{item[0]:<20} {item[1]:<50} {item[2]:<30} {item[3]:<25} {item[4]:<8} {item[5]:<12} {item[6]:<8.2f} {item[7]:<8}")
        else:
            print(f"No results found for '{Title}'.")
        
        input("\nPress Enter to return to the inventory menu.")


    def decreaseStock(self, ISBN, Quantity=1):

        query = "UPDATE inventory SET Stock = Stock - ? WHERE ISBN = ?"
        self.cursor.execute(query, (Quantity, ISBN))
        self.connection.commit()

    def close(self):
        self.connection.close()
