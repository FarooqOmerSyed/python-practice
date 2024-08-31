def calculate_total_cost(menu):
    total_cost = 0
    while True:
        user_input = input('Enter your food (or type "done" to finish): ').lower()
        if user_input == "done":
            break
        if user_input in menu:
            try:
                user_selection = int(input(f'Enter how many {user_input}(s): '))
                if user_selection > 6:
                    print("Enter selection's not more than 6")
                else:
                    total_cost += menu[user_input] * user_selection
                    print(f'Added {user_selection} {user_input}(s) to your order.')
                
            except ValueError:
                print('Please enter a valid number for the quantity.')
        else:
            print('ERROR: There is no such item in the menu.')
    print(f'Total cost of your order: ${total_cost}')

menu = {'wada': 3, 'idly': 2, 'dosa': 5}
calculate_total_cost(menu)
