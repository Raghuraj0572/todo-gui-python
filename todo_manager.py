import os
import json

TASK_FILE = "tasks.json"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as f:
            return json.load(f)
    return []

def save_tasks(tasks):
    with open(TASK_FILE, "w") as f:
        json.dump(tasks, f)

def show_menu():
    print("\n--- To-Do List Manager ---")
    print("1. View Tasks")
    print("2. Add Task")
    print("3. Mark Task as Complete")
    print("4. Delete Task")
    print("5. Exit")

def view_tasks(tasks):
    if not tasks:
        print("No tasks found.")
        return
    for i, task in enumerate(tasks, start=1):
        status = "✅" if task['done'] else "❌"
        print(f"{i}. {task['title']} [{status}]")

def add_task(tasks):
    title = input("Enter task title: ")
    tasks.append({"title": title, "done": False})
    print("Task added.")

def mark_complete(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to mark complete: ")) - 1
        if 0 <= index < len(tasks):
            tasks[index]['done'] = True
            print("Task marked as complete.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def delete_task(tasks):
    view_tasks(tasks)
    try:
        index = int(input("Enter task number to delete: ")) - 1
        if 0 <= index < len(tasks):
            tasks.pop(index)
            print("Task deleted.")
        else:
            print("Invalid task number.")
    except ValueError:
        print("Enter a valid number.")

def main():
    tasks = load_tasks()
    while True:
        show_menu()
        choice = input("Choose an option: ")
        if choice == "1":
            view_tasks(tasks)
        elif choice == "2":
            add_task(tasks)
        elif choice == "3":
            mark_complete(tasks)
        elif choice == "4":
            delete_task(tasks)
        elif choice == "5":
            save_tasks(tasks)
            print("Tasks saved. Exiting...")
            break
        else:
            print("Invalid choice. Try again.")

if __name__ == "__main__":
    main()
