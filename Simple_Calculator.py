import tkinter as tk
from tkinter import messagebox

def perform_calculation():
    try:
        num1 = float(entry_num1.get())
        num2 = float(entry_num2.get())
        operation = operation_var.get()

        if operation == '+':
            result = num1 + num2
        elif operation == '-':
            result = num1 - num2
        elif operation == '*':
            result = num1 * num2
        elif operation == '/':
            if num2 == 0:
                messagebox.showerror("Error", "Division by zero is not allowed.")
                return
            result = num1 / num2
        else:
            messagebox.showerror("Error", "Please select a valid operation.")
            return

        label_result.config(text=f"Result: {result}")
    except ValueError:
        messagebox.showerror("Error", "Invalid input. Please enter numeric values.")

def exit_application():
    root.destroy()

# Create the main window
root = tk.Tk()
root.title("Simple Calculator")
root.configure(bg="#131323")

# Create input fields and labels
label_num1 = tk.Label(root, text="Enter the First Number :", bg="#131323", fg="#ffffff", font=("Arial", 12))
label_num1.grid(row=0, column=0, padx=10, pady=5, sticky="e")
entry_num1 = tk.Entry(root, font=("Arial", 12))
entry_num1.grid(row=0, column=1, padx=10, pady=5)

label_num2 = tk.Label(root, text="Enter the Second Number :", bg="#131323", fg="#ffffff", font=("Arial", 12))
label_num2.grid(row=1, column=0, padx=10, pady=5, sticky="e")
entry_num2 = tk.Entry(root, font=("Arial", 12))
entry_num2.grid(row=1, column=1, padx=10, pady=5)

label_operation = tk.Label(root, text="Select an Operation :", bg="#131323", fg="#ffffff", font=("Arial", 12))
label_operation.grid(row=2, column=0, padx=10, pady=5, sticky="e")
operation_var = tk.StringVar(value='+')

# Create radio buttons for operation selection
radio_add = tk.Radiobutton(root, text="Addition (+)", variable=operation_var, value='+', bg="#131323", fg="#ffffff", font=("Arial", 12), selectcolor="#333333")
radio_add.grid(row=2, column=1, sticky="w")
radio_sub = tk.Radiobutton(root, text="Subtraction (-)", variable=operation_var, value='-', bg="#131323", fg="#ffffff", font=("Arial", 12), selectcolor="#333333")
radio_sub.grid(row=3, column=1, sticky="w")
radio_mul = tk.Radiobutton(root, text="Multiplication (*)", variable=operation_var, value='*', bg="#131323", fg="#ffffff", font=("Arial", 12), selectcolor="#333333")
radio_mul.grid(row=4, column=1, sticky="w")
radio_div = tk.Radiobutton(root, text="Division (/)", variable=operation_var, value='/', bg="#131323", fg="#ffffff", font=("Arial", 12), selectcolor="#333333")
radio_div.grid(row=5, column=1, sticky="w")

# Create a calculate button
button_calculate = tk.Button(root, text="Calculate", command=perform_calculation, bg="#4682b4", fg="#ffffff", font=("Arial", 12, "bold"), relief="raised", bd=2)
button_calculate.grid(row=6, column=0, columnspan=2, pady=10)

# Create an exit button
button_exit = tk.Button(root, text="Exit", command=exit_application, bg="#b22222", fg="#ffffff", font=("Arial", 12, "bold"), relief="raised", bd=2)
button_exit.grid(row=8, column=0, columnspan=2, pady=10)

# Create a label to display the result
label_result = tk.Label(root, text="Result: ", bg="#131323", fg="#ffffff", font=("Arial", 14, "bold"), relief="groove", padx=10, pady=5)
label_result.grid(row=7, column=0, columnspan=2, pady=10)

# Run the application
root.mainloop()


# THANK YOU #