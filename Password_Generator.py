import tkinter as tk
from tkinter import messagebox
import random
import string

def generate_password():
    try:
        length = int(entry_length.get())
        if length <= 3:
            messagebox.showerror("Error", "Password length must be greater than 3")
            return
        
        characters = string.ascii_letters + string.punctuation + string.digits
        password = ''.join(random.choice(characters) for _ in range(length))
        entry_password.delete(0, tk.END)
        entry_password.insert(0, password)
    except ValueError:
        messagebox.showerror("Error", "Please enter a valid number for password length")

def copy_to_clipboard():
    root.clipboard_clear()
    root.clipboard_append(entry_password.get())
    root.update()
    messagebox.showinfo("Copied", "Password copied to clipboard")

def exit_app():
    root.destroy()

# Create main window
root = tk.Tk()
root.title("Password Generator")
root.geometry("400x200")
root.configure(bg='#131323')
root.resizable(False, False)

# UI Elements
tk.Label(root, text="Enter Password Length:", fg='#ffffff', bg='#131323', font=("Arial", 12)).pack(pady=5)
entry_length = tk.Entry(root)
entry_length.pack(pady=5)

generate_btn = tk.Button(root, text="Generate Password", command=generate_password)
generate_btn.pack(pady=5)

entry_password = tk.Entry(root, width=40)
entry_password.pack(pady=5)

copy_btn = tk.Button(root, text="Copy to Clipboard", command=copy_to_clipboard)
copy_btn.pack(pady=5)

exit_btn = tk.Button(root, text="Exit", command=exit_app)
exit_btn.pack(pady=5)

# Run application
root.mainloop()


# THANK YOU #