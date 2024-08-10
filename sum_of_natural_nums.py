# Sum of natural numbers up to a user-defined input
def sum_of_natural_nums():
    user_input = int(input('Enter a positive number: '))
    result = sum(range(1, user_input + 1))
    print(f"The sum of natural numbers up to {user_input} is: {result}")

sum_of_natural_nums()
