def generate_invoice():
    
    items = {
        'idly': 20,
        'wada': 30,
        'dosa': 50,
        'upma': 40
    }
    
    total_bill = 0 
    ordered_items = []
    
    while True:
        item = input('Enter your food item( quit to exit):')
        if item.lower() == 'quit':
            break
        if item in items:
            quantity = int(input('Enter your quantity:'))
            ordered_items.append((item, quantity))
            total_bill += items[item] * quantity
            print(f"{item}: {items[item]} x {quantity} =  { items[item] * quantity}")
        else:
            print('Invalid item try again')
            
    print("\nInvoice")
    for item, quantity in ordered_items:
        print(f"{item}: {items[item]} x {quantity} =  { items[item] * quantity}")
    print(f"TOTAL : {total_bill}")
        
    
if __name__ == "__main__":
    generate_invoice()
    