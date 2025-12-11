import tkinter as tk
from tkinter import ttk
def check_strength():
    password = entry.get()
    length = len(password)
    if length == 0:
        strength = "please enter a password."
        color = "black"
    elif length < 6:
        strength = "weak"
        color = "red"
    elif length < 10:
        strength = "medium"
        color = "orange"
    else:
        strength = "strong"
        color = "green"
    result_label.config(text=strength, foreground=color)
root = tk.Tk()
root.title("password strength checker")
root.geometry("350x180")
label = ttk.Label(root, text="enter password:")
label.pack(pady=10)
entry = ttk.Entry(root, show="*", width=30)
entry.pack()
button = ttk.Button(root, text="check strength", command=check_strength)
button.pack(pady=10)
result_label = ttk.Label(root, text="", font=("Arial", 12, "bold"))
result_label.pack(pady=10)
root.mainloop()