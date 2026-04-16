import json
import os

FILE = "tasks.json"

# Load tasks
def load_tasks():
    if os.path.exists(FILE):
        with open(FILE, "r") as f:
            return json.load(f)
    return []

# Save tasks
def save_tasks(tasks):
    with open(FILE, "w") as f:
        json.dump(tasks, f, indent=4)

# Add task
def add_task(tasks):
    task = input("Enter task: ")
    tasks.append({"task": task, "done": False})
    save_tasks(tasks)

# View tasks
def view_tasks(tasks):
    if not tasks:
        print("No tasks available")
        return
    for i, t in enumerate(tasks):
        status = "✔" if t["done"] else "✘"
        print(f"{i+1}. {t['task']} [{status}]")

# Delete task
def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        tasks.pop(index)
        save_tasks(tasks)
    except:
        print("Invalid input")

# Mark done
def mark_done(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark done: ")) - 1
        tasks[index]["done"] = True
        save_tasks(tasks)
    except:
        print("Invalid input")

# Main loop
tasks = load_tasks()

while True:
    print("\n1.Add 2.View 3.Delete 4.Mark Done 5.Exit")
    choice = input("Choose: ")

    if choice == "1":
        add_task(tasks)
    elif choice == "2":
        view_tasks(tasks)
    elif choice == "3":
        delete_task(tasks)
    elif choice == "4":
        mark_done(tasks)
    elif choice == "5":
        break
    else:
        print("Invalid choice")