# Longest word in a string

my_string = 'bro gonna find the longest word in the string'

# Split the string into words
splitted = my_string.split()

# Find the longest word
longest_word = max(splitted, key=len)

# Print the longest word and its length
print(f"The longest word is: '{longest_word}' with length {len(longest_word)}")
