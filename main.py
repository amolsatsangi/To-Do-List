def  add_task():
    task = input("Enter the task: ")
    with open(r"C:\Users\amols\OneDrive - Cadence Design Systems Inc\Desktop\To_do_list\To-Do-List\tasks.txt", "a") as file:
        file.writelines(task + "\n")
def complete_task():
    index = input("Enter the task number you want to complete: ")
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
def edit_task():
    index = input("Enter the task number you want to edit: ")
    new_task = input("Enter the new task: ")
    with open(r"C:\Users\amols\OneDrive - Cadence Design Systems Inc\Desktop\To_do_list\To-Do-List\tasks.txt","r") as file:
        tasks = file.readlines()
        tasks[int(index)-1] = new_task + "\n"
        
    with open(r"C:\Users\amols\OneDrive - Cadence Design Systems Inc\Desktop\To_do_list\To-Do-List\tasks.txt","w") as file:
        file.writelines(tasks)

    
while(True):
    user_action = input("What would you like to do? (add, complete, show, edit, exit): ")
    user_action=(user_action.strip()).lower()
    match user_action:
        case "add":
            add_task()
        case "complete":
            complete_task()
        case "show":
            show_tasks()
        case "edit":
            edit_task()
        case "exit":
            break
        case _:
            print("Invalid input")
