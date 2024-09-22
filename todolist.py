import tkinter as tk
from tkinter import messagebox

class TodoApp:
    def __init__(self, root):
        self.root = root
        self.root.title("To-Do List App")

        # Initialize tasks list
        self.tasks = []

        # Create GUI elements
        self.task_listbox = tk.Listbox(self.root, height=10, width=50)
        self.task_listbox.pack(pady=10)

        self.title_entry = tk.Entry(self.root, width=52)
        self.title_entry.pack()

        self.description_entry = tk.Entry(self.root, width=52)
        self.description_entry.pack()

        self.due_date_entry = tk.Entry(self.root, width=52)
        self.due_date_entry.pack()

        # Buttons
        self.add_button = tk.Button(self.root, text="Add Task", width=48, command=self.add_task)
        self.add_button.pack(pady=10)

        self.delete_button = tk.Button(self.root, text="Delete Task", width=48, command=self.delete_task)
        self.delete_button.pack()

        self.update_button = tk.Button(self.root, text="Update Task", width=48, command=self.update_task)
        self.update_button.pack(pady=10)

        # Load initial tasks
        self.load_tasks()

    def load_tasks(self):
        self.task_listbox.delete(0, tk.END)
        for task in self.tasks:
            self.task_listbox.insert(tk.END, f"{task['title']} - {task['description']} - {task['due_date']}")

    def add_task(self):
        title = self.title_entry.get()
        description = self.description_entry.get()
        due_date = self.due_date_entry.get()

        if title and description and due_date:
            self.tasks.append({'title': title, 'description': description, 'due_date': due_date})
            self.load_tasks()
            self.clear_entries()
        else:
            messagebox.showwarning("Warning", "Please fill in all fields.")

    def delete_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            self.tasks.pop(selected_index)
            self.load_tasks()
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to delete.")

    def update_task(self):
        try:
            selected_index = self.task_listbox.curselection()[0]
            title = self.title_entry.get()
            description = self.description_entry.get()
            due_date = self.due_date_entry.get()

            if title and description and due_date:
                self.tasks[selected_index] = {'title': title, 'description': description, 'due_date': due_date}
                self.load_tasks()
                self.clear_entries()
            else:
                messagebox.showwarning("Warning", "Please fill in all fields.")
        except IndexError:
            messagebox.showwarning("Warning", "Please select a task to update.")

    def clear_entries(self):
        self.title_entry.delete(0, tk.END)
        self.description_entry.delete(0, tk.END)
        self.due_date_entry.delete(0, tk.END)

if __name__ == "__main__":
    root = tk.Tk()
    app = TodoApp(root)
    root.mainloop()
