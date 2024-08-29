funcs_list = []

#Decorator Function
def run_funcs(func):
  funcs_list.append(func)
  return func 

#Decorating Funciton with Decorator Function
@run_funcs  
def func_one():
  return f"this is function one"
  
#Decorating Funciton with Decorator Function
@run_funcs    
def func_two():
  return f"this is function two"
  
#Decorating Funciton with Decorator Function  
@run_funcs    
def func_three():
  return f"this is function three"
  
#Decorating Funciton with Decorator Function  
@run_funcs    
def func_four():
  return f"this is function four"
  
#run directly as main program not when imported as module  
if __name__ == '__main__':
  #loop through funcs_list list 
  for i in funcs_list:
    #print i as method 
    print(i())
    
    

