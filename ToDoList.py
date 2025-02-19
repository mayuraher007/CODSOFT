#Task1

import json
import tkinter as tk
from tkinter import messagebox

class ToDoListApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List")

        self.tasks = []
        self.load_tasks()

        self.root.configure(bg="#f0f8ff") 

        self.task_listbox = tk.Listbox(self.root, selectmode=tk.SINGLE, width=50, height=15, bg="#ffffff", fg="#000000", selectbackground="#add8e6")
        self.task_listbox.pack(pady=10)

        self.entry_field = tk.Entry(self.root, width=50, bg="#e6f7ff", fg="#000000")
        self.entry_field.pack(pady=5)

        self.add_button = tk.Button(self.root, text="Add Task", command=self.add_task, bg="#32cd32", fg="#ffffff", activebackground="#228b22")
        self.add_button.pack(pady=5)

        self.edit_button = tk.Button(self.root, text="Edit Task", command=self.edit_task, bg="#ffa500", fg="#ffffff", activebackground="#ff8c00")
        self.edit_button.pack(pady=5)

        self.complete_button = tk.Button(self.root, text="Mark as Completed", command=self.mark_completed, bg="#4682b4", fg="#ffffff", activebackground="#4169e1")
        self.complete_button.pack(pady=5)

        self.delete_button = tk.Button(self.root, text="Delete Task", command=self.delete_task, bg="#ff4500", fg="#ffffff", activebackground="#dc143c")
        self.delete_button.pack(pady=5)

        self.display_tasks()

    def load_tasks(self):
        """Loads tasks from a file (if it exists)."""
        try:
            with open("tasks.json", "r") as file:
                self.tasks = json.load(file)
        except FileNotFoundError:
            self.tasks = []

    def save_tasks(self):
        """Saves tasks to a file."""
        with open("tasks.json", "w") as file:
            json.dump(self.tasks, file)

    def add_task(self):
        """Adds a new task to the list."""
        task = self.entry_field.get().strip()
        if task:
            self.tasks.append({"task": task, "completed": False})
            self.save_tasks()
            self.entry_field.delete(0, tk.END)
            self.display_tasks()
        else:
            messagebox.showwarning("Input Error", "Please enter a task.")

    def display_tasks(self):
        """Displays all tasks in the listbox."""
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            status = "[x]" if task["completed"] else "[ ]"
            self.task_listbox.insert(tk.END, f"{status} {task['task']}")

    def mark_completed(self):
        """Marks the selected task as completed."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            self.tasks[index]["completed"] = True
            self.save_tasks()
            self.display_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to mark as completed.")

    def delete_task(self):
        """Deletes the selected task from the list."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            del self.tasks[index]
            self.save_tasks()
            self.display_tasks()
        else:
            messagebox.showwarning("Selection Error", "Please select a task to delete.")

    def edit_task(self):
        """Edits the selected task."""
        selected_index = self.task_listbox.curselection()
        if selected_index:
            index = selected_index[0]
            current_task = self.tasks[index]["task"]
            new_task = self.entry_field.get().strip()
            if new_task:
                self.tasks[index]["task"] = new_task
                self.save_tasks()
                self.display_tasks()
                self.entry_field.delete(0, tk.END)
            else:
                messagebox.showwarning("Input Error", "Please enter a new task description.")
        else:
            messagebox.showwarning("Selection Error", "Please select a task to edit.")


if __name__ == "__main__":
    root = tk.Tk()
    app = ToDoListApp(root)
    root.mainloop()
