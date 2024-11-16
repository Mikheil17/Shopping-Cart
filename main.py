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
            print("...")

        # If the user enters an invalid option
        else:
            print("That's not a menu option. Please try again.")
        
        print()  # Newline for better formatting

def inventoryMenu(inventory):
    while True:
        print("\nInventory Menu:")
        print("0. Return to Main Menu")
        print("1. View All Inventory")
        print("2. View Inventory by User")
        print("3. Add New Item to Inventory")
        print("4. Update Item in Inventory")
        print("5. Remove Item from Inventory")

        option = input("Enter your menu choice: ")
        print()

        if option == "0":
            print("Returning to main menu...")
            break  # Exit to main menu

        elif option == "1":
            print("Viewing all inventory...")
            inventory_list = inventory.viewInventory()  # Fetch inventory data
            if inventory_list:
                print("Inventory List:")
                print(f"{'ISBN':<20} {'Title':<50} {'Author':<30} {'Genre':<20} {'Pages':<10} {'Price':<10} {'Stock':<10}")
                for item in inventory_list:
                    # Ensure the ISBN is displayed correctly
                    print(f"{item[1]:<20} {item[2]:<50} {item[3]:<30} {item[4]:<20} {item[5]:<10} {item[6]:<10} {item[7]:<10}")
            else:
                print("No inventory items found.")
            input("Press Enter to return to the inventory menu.")  # Pause to allow the user to view the inventory
            print()  # Newline for better formatting

        elif option == "2":
            print("Viewing inventory for a specific user...")
            userID = input("Enter User ID: ")
            inventory_list = inventory.viewInventory(userID)  # Fetch user-specific inventory
            if inventory_list:
                print("User Inventory List:")
                print(f"{'ISBN':<20} {'Title':<50} {'Author':<30} {'Genre':<20} {'Pages':<10} {'Price':<10} {'Stock':<10}")
                for item in inventory_list:
                    # Ensure the ISBN is displayed correctly
                    print(f"{item[1]:<20} {item[2]:<50} {item[3]:<30} {item[4]:<20} {item[5]:<10} {item[6]:<10} {item[7]:<10}")
            else:
                print(f"No inventory found for User ID {userID}.")
            input("Press Enter to return to the inventory menu.")  # Pause
            print()

        elif option == "3":
            print("Adding a new item to inventory...")
            userID = input("Enter your User ID: ")
            ISBN = input("Enter the ISBN of the book: ")
            
            # Ensure the ISBN is not empty
            if not ISBN:
                print("ISBN cannot be empty. Please try again.")
                continue  # Skip to the next iteration of the loop
            
            # Validate numeric input for quantity and cost
            try:
                quantity = int(input("Enter the quantity: "))
                cost = float(input("Enter the cost of the book: "))
                
                # Call the method to add to inventory
                inventory.addToInventory(userID, ISBN, quantity, cost)
                print("Item successfully added to the inventory.")
            except ValueError:
                print("Invalid input. Please enter valid numeric values for quantity and cost.")
            
            input("Press Enter to return to the inventory menu.")
            print()

        elif option == "4":
            print("Updating an inventory item...")
            # This is where you'll implement the logic for updating an inventory item (e.g., price, quantity)
            print("Feature not yet implemented.")
            input("Press Enter to return to the inventory menu.")
            print()

        elif option == "5":
            print("Removing an item from inventory...")
            ISBN = input("Enter the ISBN of the item to remove: ")
            # Implement the logic for removing an inventory item based on ISBN
            print("Feature not yet implemented.")
            input("Press Enter to return to the inventory menu.")
            print()

        else:
            print("Invalid option. Please try again.")



def main():
    print("Welcome to the online bookstore!\n")

    initialMenu()

main()
