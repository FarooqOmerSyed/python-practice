functions = []

def runner(func):
    functions.append(func)
    return func

@runner
def func_one():
    return "this is function one"

@runner    
def func_two():
    return "this is function two"

@runner   
def func_three():
    return "this is function three"
    
if __name__ == '__main__':
    for result in map(lambda f: f(), functions):
        print(result)
