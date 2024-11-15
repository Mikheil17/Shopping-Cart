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

        # Option 1: Account Information
        elif option == "1":
            print("...")

        # Option 2: Inventory Information -- Only have viewInventory completed, but can organize it better.
        elif option == "2":
           
            inventory_list = inventory.viewInventory()  # Fetch inventory data
            if inventory_list:
                print("Inventory List:")
                print(f"{'ISBN':<20} {'Title':<50} {'Author':<30} {'Genre':<20} {'Pages':<10} {'Price':<10} {'Stock':<10}")
                for item in inventory_list:
                    print(f"{item[1]:<20} {item[2]:<50} {item[3]:<30} {item[4]:<20} {item[5]:<10} {item[6]:<10} {item[7]:<10}")
            else:
                print("No inventory items found.")
            input("Press Enter to return to the main menu.")  # Pause to allow the user to view the inventory
            print()  # Newline for better formatting

        # Option 3:Cart Information
        elif option == "3":
            print("...")

        # Option 4: Order Information
        elif option == "4":
            print("...")

        # If the user enters an invalid option
        else:
            print("That's not a menu option. Please try again.")
        
        print()  # Newline for better formatting



def main():
    print("Welcome to the online bookstore!\n")

    initialMenu()

main()
