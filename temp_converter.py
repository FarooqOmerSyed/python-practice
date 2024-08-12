# temperature converter 

def temp_converter():
    user_input = str(input('what do you want to convert c to f or f to c ? :'))
    if user_input == 'c':
        cel_input = int(input('enter your celsius :'))
        cel_result = (cel_input * 9/5) + 32
        print(f"converted temp to {cel_result:.2f} F")
    elif user_input == 'f':
        fah_input = int(input('enter your fahrenheit :'))
        fah_result = (fah_input - 32) * 5/9
        print(f"converted temp to {fah_result:.2f} C")
        

temp_converter()