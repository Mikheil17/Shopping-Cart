from user import *
from cart import *
from inventory import *
from history import *


## COMPLETE initial pre-login menu
def initialMenu():
    ## objects for the classes
    user = User()
    cart = Cart()
    inventory = Inventory()
    history = OrderHistory()

    ## initial menu
    while(1):
        print("Pre-Login Menu:")
        print("0. Login")
        print("1. Create Account")
        print("2. Exit Program")
        initial = input("Enter your menu choice: ")
        print()

        if(initial == "0"):
            user.login()

        elif(initial == "1"):
            user.createAccount()

        ## exit program
        elif(initial == "2"):
            print("Good-bye!")
            break

        ## incorrect menu option
        else:
            print("That's not a menu option. Please try again.")

        print()

        ## checks status after one menu loop...
        ## goes into main menu if applicable
        if(user.getLoggedIn()):
            mainMenu(user, cart, inventory, history)


## incomplete main menu...
def mainMenu(user, cart, inventory, history):
    while user.getLoggedIn():  # Loop while the user is logged in
        print("Main Menu:")
        print("0. Logout")
        print("1. View Account Information")
        print("2. Inventory Information")  # Option for viewing inventory
        print("3. Cart Information")
        print("4. Order Information")
        
        # User input to select an option
        option = input("Enter your menu choice: ")
        print()

        # Option 0: Logout
        if option == "0":
            user.logout()  # Log the user out
            print("Successful logout.")
            break  # Exit the loop and go back to the initial menu (or exit program)

        # Option 1: View Account Information
        elif option == "1":
            print("...")

        # Option 2: View Inventory Information
        elif option == "2":
            print("Opening Inventory...")
            inventoryMenu(inventory)  # Open the inventory menu

        # Option 3: View Cart Information
        elif option == "3":
            print("...")

        # Option 4: View Order Information
        elif option == "4":
            print("Entering Order History...")
            ordersMenu(user, history) # Opens the order management and history menu
            

        # If the user enters an invalid option
        else:
            print("That's not a menu option. Please try again.")
        
        print()  # Newline for better formatting

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
                print(f"\nSearch Results:")
                print(f"{'ISBN':<20} {'Title':<50} {'Author':<30} {'Genre':<25} {'Pages':<8} {'Price':<8} {'Stock':<8}")
                print("-" * 150)
                for item in inventory_list:
                    print(f"{item[0]:<20} {item[1]:<50} {item[2]:<30} {item[3]:<25} {item[4]:<8} {item[5]:<8.2f} {item[6]:<8}")
            else:
                print(f"No results found for '{Title}'.")
            input("\nPress Enter to return to the inventory menu.")

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

def ordersMenu(user, history):
    while True:
        print("\nOrders and History:")
        print("0. Return to Main Menu")
        print("1. View Order History")
        print("2. View Order")

        option = input("Enter your menu choice: ").strip()
        print()

        if option == "0":
            print("Returning to main menu...")
            break
        
        elif option == "1": # Viewing their order history
            print("Viewing your orders...")
            OrderHistory.viewHistory(user.userID)
        
        elif option == "2": # Viewing an order
            individualOrder = input("Please enter the ID of the order you wish to view: ").strip()
            print("Finding your order...")
            OrderHistory.viewOrder(user.userID, individualOrder)
        
        else:
            print("Invalid option. Please try again.")


def main():
    print("Welcome to the online bookstore!\n")

    initialMenu()

main()
