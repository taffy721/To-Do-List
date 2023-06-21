file_path = r'C:\Users\HP\Documents\todolist\list.txt'

def add():
    taskname = input("Task: ")
    startdate = input("Start date: ")
    enddate = input("End date: ")
    new_task = f"Task: {taskname}, Start date: {startdate}, End date: {enddate}\n"

    with open(file_path, 'a') as file:
        file.write(new_task)


def view():
    with open(file_path, 'r') as file:
        tasks = file.readlines()

    name = input("Enter task: ")
    for task in tasks:
        if name in task:
            task = task.replace("[", "").replace("]","")
            task = task.replace("\n", "")
            print(task)

def delete_line():
    with open(file_path, 'r') as file:
        lines = file.readlines()

    name = input("Enter task: ")
    confirmed = input("Are you sure you want to continue? Your task will be deleted. (y/n): ")
    confirmed = confirmed.lower() 

    if confirmed == "y":
        with open(file_path, 'w') as file:
            for line in lines:
                if name not in line:
                    file.write(line)
        print("Task", name, "has been completed.")
    else:
        print("Task status is unchanged")

while True:
    print("What would you like to do?")
    print("1.Add a task")
    print("2.View a task")
    print("3.Change a task status")
    print("4.Quit")

    choice = input("Choose option (1-4): ")

    if choice == "1":
        add()
    if choice == "2":
        view()
    if choice == "3":
        delete_line()
    if choice == "4":
        break