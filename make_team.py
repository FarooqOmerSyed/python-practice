user_data = []
task_funcs = []
user_team = ""

#decorator function
def runner(func):
    task_funcs.append(func)
    return func
    
@runner
def add_users():
    global user_team
    user_team = input('Enter team name:')
    
    while True:
        user_input = input('Enter player name (quit to exit):')
        if user_input.lower() == 'quit':
            break
        else:
            user_data.append(user_input)
            print(f"{user_input} has been added!! to team {user_team}")
            
@runner
def print_users():
    print(f"List of player in team {user_team} :")
    for i, user in enumerate(user_data, start=1):
        print(i, user)

if __name__ == '__main__':
    for func in task_funcs:
        func()
        
        
            

