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
        print("2. Inventory Information")
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
            print("Viewing your account information...")
            user.viewAccountInformation()  # View the account information


        # Option 2: View Inventory Information
        elif option == "2":
            print("Opening Inventory...")
            inventoryMenu(inventory)  # Open the inventory menu

        # Option 3: View Cart Information
        elif option == "3":
            print("Viewing Cart Information...")
            cartMenu(user, cart) # Open the cart information menu

        # Option 4: View Order Information
        elif option == "4":
            print("Entering Order History...")
            ordersMenu(user, history) # Opens the order management and history menu
            

        # If the user enters an invalid option
        else:
            print("That's not a menu option. Please try again.")
        
        print()  # Newline for better formatting


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
            OrderHistory.viewHistory(history, user.userID)
        
        elif option == "2": # Viewing an order
            individualOrder = input("Please enter the ID of the order you wish to view: ")
            print("Finding your order...")
            OrderHistory.viewOrder(history, user.userID, individualOrder)
        
        else:
            print("Invalid option. Please try again.")

def cartMenu(user, cart):
    while True:
        print("\nCart Menu:")
        print("0. Return to Main Menu")
        print("1. View Cart")
        print("2. Add Item to Cart")
        print("3. Remove Item from Cart")
        print("4. Edit Item Quantity in Cart")
        print("5. Checkout")

        option = input("Enter your menu choice: ").strip()
        print()

        if option == "0":
            print("Returning to main menu...")
            break

        elif option == "1":  # View Cart
            print("Viewing your cart...")
            cart.viewCart(user.userID)  # Display the items in the user's cart

        elif option == "2":  # Add Item to Cart
            print("Adding item to your cart...")
            ISBN = input("Enter the ISBN of the item to add: ").strip()
            try:
                quantity = int(input("Enter the quantity to add: ").strip())
                if quantity <= 0:
                    print("Quantity must be greater than 0.")
                else:
                    cart.addToCart(user.userID, ISBN, quantity)  # Add item to the cart
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")

        elif option == "3":  # Remove Item from Cart
            print("Removing item from your cart...")
            ISBN = input("Enter the ISBN of the item to remove: ").strip()
            cart.removeFromCart(user.userID, ISBN)  # Remove the item from the cart

        elif option == "4":  # Edit Item Quantity
            print("Editing item quantity in your cart...")
            ISBN = input("Enter the ISBN of the item to edit: ").strip()
            try:
                new_quantity = int(input("Enter the new quantity: ").strip())
                if new_quantity <= 0:
                    print("Quantity must be greater than 0.")
                else:
                    # Update the quantity by setting the new value
                    cart.addToCart(user.userID, ISBN, new_quantity)
                    print(f"Quantity for ISBN {ISBN} updated to {new_quantity}.")
            except ValueError:
                print("Invalid quantity. Please enter a valid number.")

        elif option == "5":  # Checkout
            print("Proceeding to checkout...")
            cart.checkOut(user.userID)  # Checkout the items in the cart

        else:
            print("Invalid option. Please try again.")

        print()

def inventoryMenu(inventory):
    while True:
        print("\nInventory Menu:")
        print("0. Return to Main Menu")
        print("1. View All Inventory")
        print("2. Search Inventory by Title")

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

        else:
            print("Invalid option. Please try again.")

def main():
    print("Welcome to the online bookstore!\n")

    initialMenu()

main()
