import tkinter as tk
from tkinter import messagebox

def calculate_interest():
    try:
        principal = float(entry_principal.get())
        rate = float(entry_rate.get())
        time = float(entry_time.get())
        simple_interest = (principal * rate * time) / 100
        compound_amount = principal * (1 + rate/100) ** time
        compound_interest = compound_amount - principal
        label_si_value.config(text=f"{simple_interest:.2f}")
        label_ci_value.config(text=f"{compound_interest:.2f}")
    except ValueError:
        messagebox.showerror("invalid input", "please enter valid numeric values.")
root = tk.Tk()
root.title("interest calculator")
root.geometry("650x600")
tk.Label(root, text="principal amount :").pack(pady=5)
entry_principal = tk.Entry(root)
entry_principal.pack()
tk.Label(root, text="rate of interest :").pack(pady=5)
entry_rate = tk.Entry(root)
entry_rate.pack()
tk.Label(root, text="time period :").pack(pady=5)
entry_time = tk.Entry(root)
entry_time.pack()
tk.Button(root, text="calculate interest", command=calculate_interest, bg="lightblue").pack(pady=15)
tk.Label(root, text="simple interest:").pack()
label_si_value = tk.Label(root, text="0.00", fg="blue")
label_si_value.pack()
tk.Label(root, text="compound interest:").pack()
label_ci_value = tk.Label(root, text="0.00", fg="green")
label_ci_value.pack()
root.mainloop()