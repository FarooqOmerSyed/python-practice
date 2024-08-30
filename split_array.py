#split the array into two halfs and add the other to anothers end
def split_add(arr: list, v: int) -> list:
    if v > len(arr):
        print('error')
    else:
         start_split = arr[:v]
         end_split = arr[v:]
    
   
    result = end_split + start_split
    return result

user_array = input('Enter your array (comma-separated values): ').split(',')
user_array = [int(i) for i in user_array]  # Convert input to a list of integers
split_value = int(input('Enter the value: '))

print(split_add(user_array, split_value))
