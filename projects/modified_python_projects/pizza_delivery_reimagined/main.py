import time

def print_welcome():
    print("""
    ============================================
         🍕 WELCOME TO PYTHON PIZZA DELIVERIES! 🍕
    ============================================
    """)

def get_pizza_size():
    while True:
        print("\nChoose your pizza size:")
        print("1. Small ($15)")
        print("2. Medium ($20)")
        print("3. Large ($25)")
        choice = input("Enter 1, 2, or 3: ").strip().lower()
        if choice == "1" or choice == "small":
            return "small", 15
        elif choice == "2" or choice == "medium":
            return "medium", 20
        elif choice == "3" or choice == "large":
            return "large", 25
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

def get_pizza_ingredient():
    while True:
        print("\nChoose your topping:")
        print("1. Pepperoni (+$3)")
        print("2. Beef (+$3)")
        print("3. Chicken (+$3)")
        choice = input("Enter 1, 2, or 3: ").strip().lower()
        if choice == "1" or choice == "pepperoni":
            return "pepperoni", 3
        elif choice == "2" or choice == "beef":
            return "beef", 3
        elif choice == "3" or choice == "chicken":
            return "chicken", 3
        else:
            print("❌ Invalid choice. Please select 1, 2, or 3.")

def get_extra_sauce():
    while True:
        print("\nDo you want extra sauce? (+$1 each)")
        print("1. Yes")
        print("2. No")
        choice = input("Enter 1 or 2: ").strip().lower()
        if choice == "1" or choice == "yes":
            while True:
                try:
                    amount = int(input("How many extra sauces? "))
                    if amount >= 0:
                        return amount
                    else:
                        print("❌ Please enter a non-negative number.")
                except ValueError:
                    print("❌ Please enter a valid number.")
        elif choice == "2" or choice == "no":
            return 0
        else:
            print("❌ Invalid choice. Please enter 1 or 2.")

def calculate_total(size_price, topping_price, extra_sauce_count):
    return size_price + topping_price + extra_sauce_count

def print_receipt(size, ingredient, extra_count, total):
    print("\n" + "="*40)
    print("           🍕 YOUR ORDER RECEIPT 🍕")
    print("="*40)
    print(f"Size: {size.capitalize()}")
    print(f"Topping: {ingredient.capitalize()}")
    print(f"Extra Sauces: {extra_count}")
    print(f"Total: ${total}")
    print("="*40)
    print("Thank you for ordering! Your pizza will be ready soon. 🚀")

def main():
    print_welcome()
    size, size_price = get_pizza_size()
    ingredient, topping_price = get_pizza_ingredient()
    extra_count = get_extra_sauce()
    total = calculate_total(size_price, topping_price, extra_count)
    print_receipt(size, ingredient, extra_count, total)

if __name__ == "__main__":
    main()