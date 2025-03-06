from manager import FruitManager
from customer import Customer

def main_menu():
    """Displays the main menu to choose roles."""
    print("\n=== WELCOME TO FRUIT MARKET ===")
    print("1) Manager")
    print("2) Customer")
    print("3) Exit")
    return input("Select your role: ")

def main():
    """Runs the program and handles role selection."""
    manager = FruitManager()
    customer = Customer()

    while True:
        choice = main_menu()
        if choice == "1":
            manager.run()
        elif choice == "2":
            customer.run()
        elif choice == "3":
            print("Thank you for using Fruit Market!")
            break
        else:
            print("Invalid choice! Please try again.")

main()  # Execute main function directly
