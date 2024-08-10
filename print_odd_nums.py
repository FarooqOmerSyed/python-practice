# odd numbers in 1 to 100

def print_odd_nums():
    user_input = int(input('enter the positive number :'))
    odd_nums = [num for num in range(1, user_input+1) if num % 2 != 0]
    print(odd_nums)
    

print_odd_nums()