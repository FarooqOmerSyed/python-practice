def vowel_count():
    vowels = ['a', 'e', 'i', 'o', 'u']
    count = 0
    user_input = input('Enter your string: ')
    for char in user_input:
        if char.lower() in vowels:
            count += 1
    if count == 0:
        print("Not a vowel")
    else:
        print(f"Number of vowels: {count} and is vowel")

vowel_count()
