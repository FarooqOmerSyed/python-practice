# print numbers from 1 to 100
# numbers = [number * 1 for number in range(1, 101)]
# print(numbers)

def num_gen():
    for num in range(1, 101):
        yield num 
        
gen = num_gen()       
print(next(gen))
print(next(gen))