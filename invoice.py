# Define the menu items and their prices
menu = {
    "Burger": 150,
    "Pizza": 250,
    "Pasta": 200
}

def display_menu():
    print("Menu:")
    for item, price in menu.items():
        print(f"{item}: ₹{price}")

def get_order():
    order = {}
    while True:
        item = input("Enter the food item you want to order (or type 'done' to finish): ")
        if item.lower() == 'done':
            break
        if item in menu:
            quantity = int(input(f"How many {item}s would you like to order? "))
            if item in order:
                order[item] += quantity
            else:
                order[item] = quantity
        else:
            print("Sorry, we don't have that item on the menu.")
    return order

def calculate_bill(order):
    total = 0
    for item, quantity in order.items():
        total += menu[item] * quantity
    return total

def print_invoice(order, total):
    print("\nInvoice:")
    for item, quantity in order.items():
        print(f"{item} x {quantity}: ₹{menu[item] * quantity}")
    print(f"Total: ₹{total}")

def main():
    display_menu()
    order = get_order()
    total = calculate_bill(order)
    print_invoice(order, total)

if __name__ == "__main__":
    main()
