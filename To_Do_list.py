from tkinter import *
from tkinter import messagebox
import sqlite3 as sql

def add_task():
    task_string = task_field.get()
    if len(task_string) == 0:
        messagebox.showinfo('Error', 'Field is Empty.')
    else:
        tasks.append(task_string)
        the_cursor.execute('INSERT INTO tasks VALUES (?)', (task_string,))
        list_update()
        task_field.delete(0, 'end')

def list_update():
    clear_list()
    for task in tasks:
        task_listbox.insert('end', task)

def delete_task():
    try:
        the_value = task_listbox.get(task_listbox.curselection())
        if the_value in tasks:
            tasks.remove(the_value)
            list_update()
            the_cursor.execute('DELETE FROM tasks WHERE title = ?', (the_value,))
    except:
        messagebox.showinfo('Error', 'No Task Selected. Cannot Delete.')

def delete_all_tasks():
    message_box = messagebox.askyesno('Delete All', 'Are you sure?')
    if message_box:
        while len(tasks) != 0:
            tasks.pop()
        the_cursor.execute('DELETE FROM tasks')
        list_update()

def clear_list():
    task_listbox.delete(0, 'end')

def close():
    print(tasks)
    guiWindow.destroy()
    the_connection.commit()
    the_cursor.close()

def retrieve_database():
    while len(tasks) != 0:
        tasks.pop()
    for row in the_cursor.execute('SELECT title FROM tasks'):
        tasks.append(row[0])

if __name__ == "__main__":
    guiWindow = Tk()
    guiWindow.title("To-Do List")
    guiWindow.geometry("800x500+500+200")
    guiWindow.resizable(0, 0)
    guiWindow.configure(bg="#F0F8FF")

    the_connection = sql.connect('listOfTasks.db')
    the_cursor = the_connection.cursor()
    the_cursor.execute('CREATE TABLE IF NOT EXISTS tasks (title TEXT)')

    tasks = []

    # Add shadow effect using ttk styles
    from tkinter import ttk
    style = ttk.Style()
    style.configure("TFrame", background="#F0F8FF")
    style.configure("TLabel", background="#F0F8FF", font=("Arial", 12))
    style.configure("TButton", font=("Arial", 12, "bold"), padding=5)

    header_frame = ttk.Frame(guiWindow, style="TFrame")
    header_frame.pack(side="top", fill="x")

    header_label = ttk.Label(
        header_frame,
        text="To-Do List App",
        font=("italic", "18", "bold"),
        foreground="white",
        background="#4682B4",
        anchor="center"
    )
    header_label.pack(pady=10, fill="x")

    input_frame = ttk.Frame(guiWindow, style="TFrame")
    input_frame.pack(pady=20)

    task_label = ttk.Label(
        input_frame,
        text="Task Title:",
        font=("Arial", "12"),
        background="#F0F8FF"
    )
    task_label.grid(row=0, column=0, padx=10, pady=5)

    task_field = ttk.Entry(
        input_frame,
        font=("Arial", "12"),
        width=40
    )
    task_field.grid(row=0, column=1, padx=10, pady=5)

    button_frame = ttk.Frame(guiWindow, style="TFrame")
    button_frame.pack(pady=10)

    add_button = ttk.Button(
        button_frame,
        text="Add Task",
        width=15,
        command=add_task,
    )
    del_button = ttk.Button(
        button_frame,
        text="Remove Task",
        width=15,
        command=delete_task,
    )
    del_all_button = ttk.Button(
        button_frame,
        text="Delete All",
        width=15,
        command=delete_all_tasks,
    )
    exit_button = ttk.Button(
        button_frame,
        text="Exit",
        width=15,
        command=close,
    )

    add_button.grid(row=0, column=0, padx=5, pady=5)
    del_button.grid(row=0, column=1, padx=5, pady=5)
    del_all_button.grid(row=0, column=2, padx=5, pady=5)
    exit_button.grid(row=0, column=3, padx=5, pady=5)

    list_frame = ttk.Frame(guiWindow, style="TFrame")
    list_frame.pack(pady=10)

    task_listbox = Listbox(
        list_frame,
        width=70,
        height=15,
        font="bold",
        selectmode='SINGLE',
        background="WHITE",
        foreground="BLACK",
        selectbackground="#4682B4",
        selectforeground="WHITE"
    )
    task_listbox.pack(side="left", fill="y")

    scrollbar = Scrollbar(list_frame, orient="vertical")
    scrollbar.config(command=task_listbox.yview)
    scrollbar.pack(side="right", fill="y")

    task_listbox.config(yscrollcommand=scrollbar.set)

    retrieve_database()
    list_update()

    guiWindow.mainloop()


# THANK YOU #