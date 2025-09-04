import json
import re

# Load tasks from tasks.json file
# If the file doesn't exist or is invalid, return an empty list
def load_tasks():
    try:
        with open("tasks.json", "r") as f:
            return json.load(f)
    except:
        return []


# Rewrite (overwrite) the tasks.json file with the updated task list
def rewrite_file(tasks):
    with open("tasks.json", "w") as f:
        json.dump(tasks, f, indent=4)


# Add a new task to the list
def add_tasks():
    tasks = load_tasks()
    priority_options = ["high", "medium", "low"]

    # Gather task details from the user
    task_name = input("Enter task name: ").lower()
    task_desc = input("Enter task description: ").lower()
    task_due = input("Enter task due date (dd/mm/yy): ").lower()

    print("Priority options: high, medium, low")
    task_priority = input("Enter task priority: ").lower()

    # Validation: priority, uniqueness, and due date format
    if task_priority in priority_options and task_name not in [t["Name"] for t in tasks] and re.match(r"\d{2}/\d{2}/\d{2}", task_due):
        tasks.append({
            "Name": task_name,
            "Description": task_desc,
            "Priority": task_priority,
            "Due": task_due,
            "Status": "Not done"
        })
        rewrite_file(tasks)
        return "Task has been added!"
    else:
        # Error handling for invalid input
        if not task_name or not task_desc or not task_due or not task_priority:
            return "Error: unable to add task"
        elif task_priority not in priority_options:
            return f"Error: {task_priority} is not a priority option"
        elif not re.match(r"\d{2}/\d{2}/\d{2}", task_due):
            return "Error: invalid date format (use dd/mm/yy)"
        elif task_name in [t["Name"] for t in tasks]:
            return f"Error: {task_name} has already been added"


# Remove a task by its position in the list
def remove_task():
    try:
        task_id = int(input("Enter task position: ")) - 1
        tasks = load_tasks()

        if 0 <= task_id < len(tasks):
            tasks.pop(task_id)
            rewrite_file(tasks)
        else:
            print("Error: Invalid task number")
    except ValueError:
        print("Error: Please enter a valid number")


# View all tasks (only shows names with index)
def view_tasks():
    tasks = load_tasks()
    task_names = []

    for i, task in enumerate(tasks, start=1):
        task_names.append(f"{i}. {task['Name']}")

    return task_names


# Mark a task as done
def mark_done():
    try:
        task_id = int(input("Enter task position: ")) - 1
        tasks = load_tasks()

        if 0 <= task_id < len(tasks):
            for task in tasks:
                if tasks[task_id] == task:
                    task["Status"] = "Done"
                    task["Name"] = task["Name"]+"*"
                    rewrite_file(tasks)
        else:
            print("Error: Invalid task number")
    except ValueError:
        print("Error: Please enter a valid number")


# Main menu for the task manager
def menu():
    while True:
        print("Menu: add / mark done / delete / view / quit")
        user_inp = input("What would you like to do?: ").lower()

        if user_inp == "add":
            new_task = add_tasks()
            print(new_task)

        elif user_inp == "view":
            print("-" * 40)
            for task in view_tasks():
                print(task)
            # Optionally view details of a specific task
            try:
                specific_task = int(input("Enter task position: ")) - 1
                if specific_task >= 0 and specific_task < len(load_tasks()):
                    tasks = load_tasks()
                    for task in tasks:
                        if tasks[specific_task] == task:
                            print("-" * 40)
                            print("Name:", task["Name"])
                            print("Description:", task["Description"])
                            print("Priority:", task["Priority"])
                            print("Due date:", task["Due"])
                            print("Status:", task["Status"])
                            print("-" * 40)
                else:
                    print("Error: Invalid task number")
            except ValueError:
                print("Error: Please enter a valid number")

        elif user_inp == "delete":
            remove_task()
            print("Task removed!")

        elif user_inp == "mark done":
            mark_done()
            print("Status has been changed!")

        elif user_inp == "quit":
            break
        else:
            print("Invalid command")


# Run the menu when the script is executed
if __name__ == "__main__":
    menu()
