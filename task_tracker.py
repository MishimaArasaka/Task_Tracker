import json
import os

tasks = []
if os.path.exists("tasks.json"):
    with open("tasks.json", "r") as f:
        tasks = json.load(f)

def save_tasks():
    with open("tasks.json", "w") as f:
        json.dump(tasks, f)

def add_tasks():
    task_name = input("Enter tasks name: ")
    tasks.append({"task": task_name, "done": False})
    save_tasks()
    print(f"Task {task_name} successfully added.")

def view_tasks():
    if not tasks:
        print("No tasks available")
    else:
        for i, t in enumerate(tasks, start=1):
            status = "Done" if t["done"] else "Not Done"
            print(f"{i}. {t['task']} - {status}")

def tasks_done():
    view_tasks()
    try:
        number = int(input("Enter task number to mark as done:"))
        tasks[number - 1]["done"] = True
        save_tasks()
        print(f"Task {number} marked as done.")
    except (ValueError, IndexError):
        print("Invalid task number.")

def delete_tasks():
    view_tasks()
    try:
        number = int(input("Enter task number to delete:"))
        tasks.pop(number - 1)
        save_tasks()
        print(f"Task {number} deleted.")
    except (ValueError, IndexError):
        print("Invalid task number.")

while True:
    print("\n===    Task Tracker    ===")
    print("1. Add Task")
    print("2. View Task")
    print("3. Mark Task")
    print("4. Delete Task")
    print("5. Exit")
    
    option = input("Choose the menu: ")
    if option == "1":
        add_tasks()
    elif option == "2":
        view_tasks()
    elif option == "3":
        tasks_done()
    elif option == "4":
        delete_tasks()
    elif option == "5":
        print("See u next time!")
        break
    else:
        print("Invalid menu")