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

def inventoryMenu(inventory):
    while True:
        print("\nInventory Menu:")
        print("0. Return to Main Menu")
        print("1. View All Inventory")
        print("2. Search Inventory by Title")
        print("3. Decrease Stock for Item")

        option = input("Enter your menu choice: ").strip()
        print()

        if option == "0":
            print("Returning to main menu...")
            break

        elif option == "1":  # View all inventory
            print("Viewing all inventory...\n")
            inventory_list = inventory.viewInventory()
            if inventory_list:
                print(f"{'ISBN':<20} {'Title':<50} {'Author':<30} {'Genre':<25} {'Pages':<8} {'ReleaseDate':<12} {'Price':<8} {'Stock':<8}")
                print("-" * 150)
                for item in inventory_list:
                    print(f"{item[0]:<20} {item[1]:<50} {item[2]:<30} {item[3]:<25} {item[4]:<8} {item[5]:<12} {item[6]:<8.2f} {item[7]:<8}")
            else:
                print("No inventory items found.")
            input("\nPress Enter to return to the inventory menu.")

        elif option == "2":  # Search inventory by title
            print("Searching inventory by title...")
            Title = input("Enter book title or part of it: ").strip()
            inventory_list = inventory.searchInventory(Title)
            if inventory_list:
                print(f"\nSearching inventory by title:")
                Title = input("Enter book title: ").strip()
                inventory.searchInventory(Title)

        elif option == "3":  # Decrease stock
            print("Decreasing stock for an item...")
            ISBN = input("Enter the ISBN of the item: ").strip()
            Quantity = input("Enter quantity to decrease: ").strip()

            try:
                Quantity = int(Quantity)
                if Quantity <= 0:
                    print("Quantity must be greater than 0.")
                    continue

                inventory.decreaseStock(ISBN, Quantity)
                print(f"Stock for ISBN '{ISBN}' successfully decreased by {Quantity}.")
            except ValueError:
                print("Invalid input. Please enter a valid number for quantity.")
            input("\nPress Enter to return to the inventory menu.")

        else:
            print("Invalid option. Please try again.")
