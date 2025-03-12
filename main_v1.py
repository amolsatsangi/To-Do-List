def  add_task(user_action):
    task = user_action[4:]
    with open(r"C:\Users\amols\OneDrive - Cadence Design Systems Inc\Desktop\To_do_list\To-Do-List\tasks.txt", "a") as file:
        file.writelines(task + "\n")
def complete_task(user_action):
    index = user_action[8:]
    with open(r"C:\Users\amols\OneDrive - Cadence Design Systems Inc\Desktop\To_do_list\To-Do-List\tasks.txt","r") as file:
        tasks = file.readlines()
        task = tasks.pop(int(index)-1)
    with open(r"C:\Users\amols\OneDrive - Cadence Design Systems Inc\Desktop\To_do_list\To-Do-List\tasks.txt","w") as file:
        file.writelines(tasks)
    task = task.strip('\n')
    print(f"Task {task} has been completed")
    
def show_tasks():
    with open(r"C:\Users\amols\OneDrive - Cadence Design Systems Inc\Desktop\To_do_list\To-Do-List\tasks.txt","r") as file:
        tasks=file.readlines()
    print()
    for i,task in enumerate(tasks):
            task = task.strip('\n')
            print(f"{i+1}. {task}")
    print()
def edit_task(user_action):
    index = int(user_action[9:])
    new_task = input("Enter the new task: ")
    with open(r"C:\Users\amols\OneDrive - Cadence Design Systems Inc\Desktop\To_do_list\To-Do-List\tasks.txt","r") as file:
        tasks = file.readlines()
        tasks[int(index)-1] = new_task + "\n"
        
    with open(r"C:\Users\amols\OneDrive - Cadence Design Systems Inc\Desktop\To_do_list\To-Do-List\tasks.txt","w") as file:
        file.writelines(tasks)

    
while(True):
    user_action = input("What would you like to do? (add, complete, show, edit, exit): ")
    user_action=(user_action.strip())
    if('add' in user_action):
            add_task(user_action)
    elif("complete" in user_action):
            complete_task(user_action)
    elif("show" in user_action):
            show_tasks()
    elif("edit" in user_action):
            edit_task(user_action)
    elif("exit" in user_action):
            break
    else:
            print("Invalid input")
