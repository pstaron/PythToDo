import tkinter as tk
from tkinter import messagebox

import tkinter as tk
from tkinter import messagebox

class TodoListApp:
    def __init__(self, master):
        self.master = master
        self.master.title("Todo List")
        self.tasks = []
        self.task_entry = tk.Entry(self.master, width=30)
        self.task_entry.pack(pady=10)
        self.add_button = tk.Button(self.master, text="Dodaj zadanie", command=self.add_task)
        self.add_button.pack(pady=5)
        self.task_listbox = tk.Listbox(self.master, width=40)
        self.task_listbox.pack(pady=10)
        self.remove_button = tk.Button(self.master, text="Usun zadanie", command=self.remove_task)
        self.remove_button.pack(pady=5)
        self.clear_button = tk.Button(self.master, text="Usun wszystkie", command=self.clear_tasks)
        self.clear_button.pack(pady=5)

        self.populate_task_listbox()

    def add_task(self):
        task = self.task_entry.get()
        if task:
            self.tasks.append(task)
            self.task_listbox.insert(tk.END, task)
            self.task_entry.delete(0, tk.END)
        else:
            messagebox.showwarning("Puste zadanie", "Wprowadz zadanie.")

    def remove_task(self):
        selected_task = self.task_listbox.curselection()
        if selected_task:
            task_index = selected_task[0]
            task = self.tasks[task_index]
            self.task_listbox.delete(task_index)
            self.tasks.remove(task)
        else:
            messagebox.showwarning("Zadanie nie wybrane", "Wybierz zadanie do usuniecia.")

    def clear_tasks(self):
        self.tasks.clear()
        self.task_listbox.delete(0, tk.END)

    def populate_task_listbox(self):
        for task in self.tasks:
            self.task_listbox.insert(tk.END, task)
            
root = tk.Tk()
todo_app = TodoListApp(root)
root.mainloop()