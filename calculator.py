import tkinter as tk
from tkinter import messagebox

# Function to evaluate the expression
def calculate():
    try:
        result = eval(entry.get())
        entry.delete(0, tk.END)
        entry.insert(tk.END, str(result))
    except Exception as e:
        messagebox.showerror("Error", "Invalid Input")

# Function to append text to the input field
def add_to_expression(value):
    entry.insert(tk.END, value)

# Function to clear the input field
def clear():
    entry.delete(0, tk.END)

# Create main window
root = tk.Tk()
root.title("Calculator")
root.geometry("300x400")
root.resizable(False, False)

# Entry field
entry = tk.Entry(root, font=("Arial", 20), border=5, relief="sunken", justify="right")
entry.pack(fill="both", padx=10, pady=10, ipady=10)

# Button layout
buttons = [
    ["7", "8", "9", "/"],
    ["4", "5", "6", "*"],
    ["1", "2", "3", "-"],
    ["0", ".", "=", "+"]
]

# Create buttons
for row in buttons:
    frame = tk.Frame(root)
    frame.pack(expand=True, fill="both")
    for char in row:
        btn = tk.Button(frame, text=char, font=("Arial", 18), height=2, command=lambda c=char: add_to_expression(c) if c != "=" else calculate())
        btn.pack(side="left", expand=True, fill="both")

# Clear button
clear_btn = tk.Button(root, text="CLEAR", font=("Arial", 16), bg="#f44336", fg="white", command=clear)
clear_btn.pack(fill="both", padx=10, pady=10)

root.mainloop()
