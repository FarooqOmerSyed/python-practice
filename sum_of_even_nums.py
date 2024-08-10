# Sum of even numbers up to a user-defined input
def sum_of_even_nums():
    user_input = int(input('Enter a positive number: '))
    even_nums = [num for num in range(1, user_input+1) if num % 2 == 0 ]
    result = sum(even_nums)
    print(f"the sum of even nums of upto user defined {user_input} is {result}")

sum_of_even_nums()
