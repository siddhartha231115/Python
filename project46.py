import tkinter as tk
from tkinter import messagebox
from datetime import date

def calculate_age():
    try:
        day = int(day_entry.get())
        month = int(month_entry.get())
        year = int(year_entry.get())
        dob = date(year, month, day)
        today = date.today()
        age_years = today.year - dob.year
        age_months = today.month - dob.month
        age_days = today.day - dob.day
        if age_days < 0:
            age_months -= 1
            last_month = (today.month - 1) if today.month > 1 else 12
            last_month_year = today.year if today.month > 1 else today.year - 1
            days_in_last_month = (date(last_month_year, last_month % 12 + 1, 1) - date(last_month_year, last_month, 1)).days
            age_days += days_in_last_month
        if age_months < 0:
            age_years -= 1
            age_months += 12
        result = f"your age: {age_years} years, {age_months} months, {age_days} days"
        messagebox.showinfo("Age Result", result)
    except Exception as E:
        messagebox.showerror("input error", "please enter a valid date!")
root = tk.Tk()
root.title("age calculator")
root.geometry("300x250")
tk.Label(root, text="enter date of birth", font=("arial", 14)).pack(pady=10)
tk.Label(root, text="day:").pack()
day_entry = tk.Entry(root)
day_entry.pack()
tk.Label(root, text="month:").pack()
month_entry = tk.Entry(root)
month_entry.pack()
tk.Label(root, text="year:").pack()
year_entry = tk.Entry(root)
year_entry.pack()
tk.Button(root, text="calculate age", command=calculate_age, bg="lightblue").pack(pady=15)
root.mainloop()