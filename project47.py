import tkinter as tk
from tkinter import messagebox
def convert_inches_to_cm():
    try:
        inches = float(inch_entry.get())
        centimeters = inches * 2.54
        result = f"{inches} inches = {centimeters:.2f} cm"
        messagebox.showinfo("result", result)
    except ValueError:
        messagebox.showerror("invalid input", "please enter a valid number!!!!!!!!!!!!!!1")
root = tk.Tk()
root.title("inches to centimeters converter")
root.geometry("300x200")
tk.Label(root, text="inches to centimeters", font=("Arial", 14)).pack(pady=10)
tk.Label(root, text="enter length in inches:").pack()
inch_entry = tk.Entry(root)
inch_entry.pack()
tk.Button(root, text="convert", command=convert_inches_to_cm, bg="lightblue").pack(pady=15)
root.mainloop()