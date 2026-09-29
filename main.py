# ==========================================================
# ONLINE FOOD ORDERING SIMULATION SYSTEM
# Developed using Python
# ==========================================================

# Food menu
menu = {
    1: {"name": "Veg Burger", "price": 120},
    2: {"name": "Pizza", "price": 250},
    3: {"name": "Veg Biryani", "price": 180},
    4: {"name": "Paneer Tikka", "price": 200},
    5: {"name": "French Fries", "price": 100},
    6: {"name": "Masala Dosa", "price": 130},
    7: {"name": "Chole Bhature", "price": 150},
    8: {"name": "Cold Drink", "price": 60},
    9: {"name": "Ice Cream", "price": 90},
    10: {"name": "Chocolate Cake", "price": 160}
}

cart = {}


# ----------------------------------------------------------
# Display menu
# ----------------------------------------------------------
def display_menu():
    print("\n" + "=" * 55)
    print("                 FOOD MENU")
    print("=" * 55)

    for item_id, item in menu.items():
        print(f"{item_id:2}. {item['name']:<25} Rs. {item['price']}")

    print("=" * 55)


# ----------------------------------------------------------
# Add food item to cart
# ----------------------------------------------------------
def add_to_cart():
    display_menu()

    try:
        item_id = int(input("Enter food item number: "))

        if item_id not in menu:
            print("Invalid food item!")
            return

        quantity = int(input("Enter quantity: "))

        if quantity <= 0:
            print("Quantity must be greater than zero.")
            return

        if item_id in cart:
            cart[item_id]["quantity"] += quantity
        else:
            cart[item_id] = {
                "name": menu[item_id]["name"],
                "price": menu[item_id]["price"],
                "quantity": quantity
            }

        print(f"{quantity} x {menu[item_id]['name']} added to cart.")

    except ValueError:
        print("Please enter a valid number.")


# ----------------------------------------------------------
# Display cart
# ----------------------------------------------------------
def display_cart():
    if not cart:
        print("\nYour cart is empty.")
        return 0

    print("\n" + "=" * 65)
    print("                         YOUR CART")
    print("=" * 65)
    print(f"{'Item':<25}{'Qty':<10}{'Price':<12}{'Amount':<12}")
    print("-" * 65)

    subtotal = 0

    for item in cart.values():
        amount = item["price"] * item["quantity"]
        subtotal += amount

        print(
            f"{item['name']:<25}"
            f"{item['quantity']:<10}"
            f"Rs. {item['price']:<9}"
            f"Rs. {amount:<10}"
        )

    print("-" * 65)
    print(f"{'Subtotal':<45} Rs. {subtotal}")
    print("=" * 65)

    return subtotal


# ----------------------------------------------------------
# Remove item from cart
# ----------------------------------------------------------
def remove_from_cart():
    if not cart:
        print("\nYour cart is empty.")
        return

    display_cart()

    try:
        item_id = int(input(
            "Enter food item number to remove: "
        ))

        if item_id not in cart:
            print("Item not found in cart.")
            return

        del cart[item_id]

        print("Item removed successfully.")

    except ValueError:
        print("Invalid input.")


# ----------------------------------------------------------
# Calculate discount
# ----------------------------------------------------------
def calculate_discount(subtotal):
    if subtotal >= 1000:
        discount = subtotal * 0.15
    elif subtotal >= 500:
        discount = subtotal * 0.10
    elif subtotal >= 300:
        discount = subtotal * 0.05
    else:
        discount = 0

    return discount


# ----------------------------------------------------------
# Calculate final bill
# ----------------------------------------------------------
def calculate_bill(subtotal):
    discount = calculate_discount(subtotal)

    after_discount = subtotal - discount

    if subtotal >= 500:
        delivery_charge = 0
    else:
        delivery_charge = 40

    tax = after_discount * 0.05

    total = after_discount + delivery_charge + tax

    return discount, delivery_charge, tax, total


# ----------------------------------------------------------
# Payment function
# ----------------------------------------------------------
def payment():
    print("\nPayment Methods")
    print("1. Cash on Delivery")
    print("2. UPI")
    print("3. Debit/Credit Card")

    try:
        choice = int(input("Choose payment method: "))

        if choice == 1:
            return "Cash on Delivery"

        elif choice == 2:
            upi = input("Enter UPI ID: ")

            if upi.strip() == "":
                print("Invalid UPI ID.")
                return None

            return "UPI"

        elif choice == 3:
            card = input("Enter last 4 digits of card: ")

            if len(card) != 4 or not card.isdigit():
                print("Invalid card details.")
                return None

            return "Debit/Credit Card"

        else:
            print("Invalid payment option.")
            return None

    except ValueError:
        print("Invalid input.")
        return None


# ----------------------------------------------------------
# Place order
# ----------------------------------------------------------
def place_order(customer_name, address):
    if not cart:
        print("\nCannot place order because cart is empty.")
        return

    subtotal = display_cart()

    discount, delivery, tax, total = calculate_bill(subtotal)

    print("\n" + "=" * 50)
    print("                   BILL")
    print("=" * 50)

    print(f"Subtotal          : Rs. {subtotal:.2f}")
    print(f"Discount          : Rs. {discount:.2f}")
    print(f"Delivery Charge   : Rs. {delivery:.2f}")
    print(f"Tax (5%)          : Rs. {tax:.2f}")
    print("-" * 50)
    print(f"TOTAL             : Rs. {total:.2f}")
    print("=" * 50)

    confirm = input("Do you want to place the order? (y/n): ")

    if confirm.lower() != "y":
        print("Order cancelled.")
        return

    method = payment()

    if method is None:
        print("Payment failed. Order not placed.")
        return

    print("\n" + "=" * 60)
    print("                 ORDER CONFIRMED")
    print("=" * 60)

    print(f"Customer Name : {customer_name}")
    print(f"Delivery To   : {address}")
    print(f"Payment       : {method}")
    print(f"Order Amount  : Rs. {total:.2f}")

    print("\nYour food will be prepared and delivered soon.")
    print("Thank you for ordering!")

    cart.clear()


# ----------------------------------------------------------
# Main program
# ----------------------------------------------------------
def main():

    print("=" * 60)
    print("       ONLINE FOOD ORDERING SIMULATION SYSTEM")
    print("=" * 60)

    customer_name = input("Enter your name: ")
    address = input("Enter delivery address: ")

    while True:

        print("\n" + "=" * 50)
        print("                    MAIN MENU")
        print("=" * 50)

        print("1. View Food Menu")
        print("2. Add Food to Cart")
        print("3. View Cart")
        print("4. Remove Item from Cart")
        print("5. Place Order")
        print("6. Exit")
        print("=" * 50)

        try:
            choice = int(input("Enter your choice: "))

            if choice == 1:
                display_menu()

            elif choice == 2:
                add_to_cart()

            elif choice == 3:
                display_cart()

            elif choice == 4:
                remove_from_cart()

            elif choice == 5:
                place_order(customer_name, address)

            elif choice == 6:
                print("\nThank you for using our Food Ordering System!")
                print("Goodbye!")
                break

            else:
                print("Please choose a number between 1 and 6.")

        except ValueError:
            print("Please enter a valid number.")


# ----------------------------------------------------------
# Program execution
# ----------------------------------------------------------

if __name__ == "__main__":
    main()
