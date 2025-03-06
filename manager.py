class FruitManager:
    #Manages fruit stock - adding, viewing and, updating.
    
    stock = {}  # Class attribute to store fruit stock

    def show_menu(self):
        #Displays the Manager menu and gets user input.
        print("\n--- Fruit Market Manager ---")
        print("1) Add Fruit Stock")
        print("2) View Fruit Stock")
        print("3) Update Fruit Stock")
        print("4) Back to Main Menu")
        return input("Enter your choice: ")

    def add_stock(self):
        #Adds new fruit stock.
        name = input("Enter fruit name: ").capitalize()
        qty = float(input("Enter quantity (kg): "))
        price = float(input("Enter price per kg: "))
        
        FruitManager.stock[name] = {"qty": qty, "price": price}
        print(f"{name} stock added successfully!")

    def view_stock(self):
        #Displays the current fruit stock.
        if not FruitManager.stock:
            print("No stock available!")
            return

        print("\n--- Current Stock ---")
        for fruit, data in FruitManager.stock.items():
            print(f"{fruit}: {data['qty']}kg - ₹{data['price']}/kg")

    def update_stock(self):
        #Updates existing fruit stock.
        self.view_stock()
        name = input("Enter fruit name to update: ").capitalize()

        if name in FruitManager.stock:
            qty = float(input("Enter new quantity (kg): "))
            price = float(input("Enter new price per kg: "))
            FruitManager.stock[name] = {"qty": qty, "price": price}
            print(f"{name} stock updated successfully!")
        else:
            print(f"{name} is not found in stock!")

    def run(self):
        #Handles the manager's operations.
        while True:
            choice = self.show_menu()
            if choice == "1":
                self.add_stock()
            elif choice == "2":
                self.view_stock()
            elif choice == "3":
                self.update_stock()
            elif choice == "4":
                break
            else:
                print("Invalid choice! Try again.")
            input("\nPress Enter to continue...")
