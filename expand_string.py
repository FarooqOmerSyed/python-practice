def expand_string(s):
    result = []
    i = 0
    
    while i < len(s):
        char = s[i]
        i += 1
        num_str = ""
        
        # Read the number following the character
        while i < len(s) and s[i].isdigit():
            num_str += s[i]
            i += 1
        
        # Expand the character based on the number
        if num_str:
            result.append(char * int(num_str))
    
    return ''.join(result)

# Input string
input_str = "a1b10"
output_str = expand_string(input_str)
print(output_str)
