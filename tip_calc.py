def tip_calculator():
    tip_value = float(0.15)
    user_input = int(input("enter your total bill: "))
    total_tip = user_input * tip_value
    print(f"${total_tip} is your tip to the total bill")
    
tip_calculator()