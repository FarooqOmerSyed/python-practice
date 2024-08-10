# program to sort string 

def sort_string():
    my_string = str(input('enter your string:'))
    result = sorted(my_string)
    print(''.join(result))
    
    
sort_string()