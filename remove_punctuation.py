import string

def remove_punc(text):
    return ''.join(char for char in text if char not in string.punctuation)
    

user_input = str(input('enter your string'))
print(remove_punc(user_input))
    