import tkinter as tk
from tkinter import messagebox
def multiply_numbers():
    try:
        num1 = float(entry1.get())
        num2 = float(entry2.get())
        result = num1 * num2
        result_label.config(text=f"Product: {result}")
    except ValueError:
        messagebox.showerror("invalid input", "please enter valid numbers.")
root = tk.Tk()
root.title("multiplication app")
root.geometry("300x200")
tk.Label(root, text="enter first number:").pack(pady=5)
entry1 = tk.Entry(root)
entry1.pack()
tk.Label(root, text="enter second number:").pack(pady=5)
entry2 = tk.Entry(root)
entry2.pack()
calc_button = tk.Button(root, text="multiply", command=multiply_numbers)
calc_button.pack(pady=10)
result_label = tk.Label(root, text="product: ")
result_label.pack()
root.mainloop()