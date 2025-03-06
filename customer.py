from manager import FruitManager  # Importing the stock management system

class Customer:
    """Allows customers to view and purchase fruits."""
    
    cart = {}  # Class attribute to store purchased fruits

    def show_menu(self):
        """Displays the Customer menu and gets user input."""
        print("\n--- Customer Menu ---")
        print("1. View Fruits")
        print("2. Purchase Fruits")
        print("3. View Cart")
        print("4. Back to Main Menu")
        return input("Enter your choice: ")

    def purchase_fruit(self):
        """Allows customers to buy fruits from stock."""
        FruitManager().view_stock()
        name = input("Enter fruit name to purchase: ").capitalize()

        if name in FruitManager.stock:
            qty = float(input("Enter quantity (kg): "))

            # Improved stock-checking logic
            if qty > FruitManager.stock[name]["qty"]:
                print("Not enough stock available!")
            else:
                # Get price and update stock
                price = FruitManager.stock[name]["price"]
                FruitManager.stock[name]["qty"] -= qty  

                # Add to cart
                Customer.cart[name] = {"qty": qty, "price": price}
                print(f"Added {qty}kg of {name} to your cart!")
        else:
            print(f"{name} is not available!")

    def view_cart(self):
        """Displays the customer's cart and total price."""
        if not Customer.cart:
            print("Cart is empty!")
            return
        
        total = 0
        print("\n--- Your Cart ---")
        for fruit, data in Customer.cart.items():
            amount = data["qty"] * data["price"]
            total += amount
            print(f"{fruit}: {data['qty']}kg x ₹{data['price']} = ₹{amount}")
        
        print(f"Total Amount: ₹{total}")

    def run(self):
        """Handles the customer's operations."""
        while True:
            choice = self.show_menu()
            if choice == "1":
                FruitManager().view_stock()
            elif choice == "2":
                self.purchase_fruit()
            elif choice == "3":
                self.view_cart()
            elif choice == "4":
                break
            else:
                print("Invalid choice! Try again.")
            input("\nPress Enter to continue...")
