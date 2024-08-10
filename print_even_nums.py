# even numbers in 1 to 100

def print_even_nums():
    user_input = int(input('enter the positive number :'))
    even_nums = [num for num in range(1, user_input+1) if num % 2 == 0]
    print(even_nums)
    

print_even_nums()