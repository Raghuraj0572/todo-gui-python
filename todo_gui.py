import tkinter as tk
from tkinter import messagebox
import os

TASK_FILE = "tasks.txt"

def load_tasks():
    if os.path.exists(TASK_FILE):
        with open(TASK_FILE, "r") as file:
            return [line.strip() for line in file.readlines()]
    return []

def save_tasks():
    with open(TASK_FILE, "w") as file:
        for task in task_listbox.get(0, tk.END):
            file.write(task + "\n")

def add_task():
    task = task_entry.get().strip()
    if task:
        task_listbox.insert(tk.END, task)
        task_entry.delete(0, tk.END)
        save_tasks()
    else:
        messagebox.showwarning("Warning", "Please enter a task.")

def delete_task():
    try:
        selected_index = task_listbox.curselection()[0]
        task_listbox.delete(selected_index)
        save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to delete.")

def mark_done():
    try:
        selected_index = task_listbox.curselection()[0]
        task = task_listbox.get(selected_index)
        if not task.startswith("✅ "):
            task = "✅ " + task
            task_listbox.delete(selected_index)
            task_listbox.insert(selected_index, task)
            save_tasks()
    except IndexError:
        messagebox.showwarning("Warning", "Please select a task to mark as done.")

# GUI setup
root = tk.Tk()
root.title("To-Do List Manager")
root.geometry("400x400")
root.resizable(False, False)

# Widgets
task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)

add_button = tk.Button(root, text="Add Task", width=20, command=add_task)
add_button.pack()

task_listbox = tk.Listbox(root, width=50, height=15)
task_listbox.pack(pady=10)

done_button = tk.Button(root, text="Mark as Done", width=20, command=mark_done)
done_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Task", width=20, command=delete_task)
delete_button.pack()

# Load tasks on start
for task in load_tasks():
    task_listbox.insert(tk.END, task)

# Run GUI
root.mainloop()
