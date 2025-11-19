import tkinter as tk

tasks = []

def add_task():
    task_text = task_entry.get()
    if task_text != "":
        var = tk.IntVar()  
        cb = tk.Checkbutton(tasks_frame, text=task_text, variable=var, onvalue=1, offvalue=0)
        cb.var = var
        cb.pack(anchor='w')
        tasks.append(cb)
        task_entry.delete(0, tk.END)

def delete_checked():
    for task in tasks[:]:
        if task.var.get() == 1:  
            task.destroy()
            tasks.remove(task)

def clear_all():
    for task in tasks[:]:
        task.destroy()
    tasks.clear()


root = tk.Tk()
root.title("To-Do List with Checkboxes")


task_entry = tk.Entry(root, width=40)
task_entry.pack(pady=10)


add_button = tk.Button(root, text="Add Task", command=add_task)
add_button.pack(pady=5)

delete_button = tk.Button(root, text="Delete Checked Tasks", command=delete_checked)
delete_button.pack(pady=5)

clear_button = tk.Button(root, text="Clear All Tasks", command=clear_all)
clear_button.pack(pady=5)


tasks_frame = tk.Frame(root)
tasks_frame.pack(pady=10)

root.mainloop()
