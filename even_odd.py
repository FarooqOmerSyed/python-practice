# program to check the user input number is even or odd

def even_odd():
    user_input = int(input('enter your number:'))
    if user_input % 2 == 0:
        print('the number is even')
    else:
        print('the number is odd')
    
even_odd()