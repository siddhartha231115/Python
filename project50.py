import tkinter as tk
import random
def play(user_choice):
    options = ["rock", "paper", "scissors"]
    computer_choice = random.choice(options)
    user_label.config(text=f"you chose: {user_choice}")
    computer_label.config(text=f"computer chose: {computer_choice}")
    if user_choice == computer_choice:
        result = "it's a tie!"
    elif (
        (user_choice == "rock" and computer_choice == "scissors") or
        (user_choice == "paper" and computer_choice == "rock") or
        (user_choice == "scissors" and computer_choice == "paper")
    ):
        result = "you win!"
    else:
        result = "computer wins!"
root = tk.Tk()
root.title("rock paper scissors game")
root.geometry("350x300")
root.config(bg="#E8F0F2")
title = tk.Label(root, text="rock paper scissors", font=("Arial", 18, "bold"), bg="#E8F0F2")
title.pack(pady=10)
user_label = tk.Label(root, text="you chose: ", font=("Arial", 12), bg="#E8F0F2")
user_label.pack()
computer_label = tk.Label(root, text="computer chose: ", font=("Arial", 12), bg="#E8F0F2")
computer_label.pack()
result_label = tk.Label(root, text="", font=("Arial", 16, "bold"), fg="blue", bg="#E8F0F2")
result_label.pack(pady=10)
button_frame = tk.Frame(root, bg="#E8F0F2")
button_frame.pack(pady=15)
rock_btn = tk.Button(button_frame, text="rock", width=10, command=lambda: play("rock"))
rock_btn.grid(row=0, column=0, padx=5)
paper_btn = tk.Button(button_frame, text="paper", width=10, command=lambda: play("paper"))
paper_btn.grid(row=0, column=1, padx=5)
scissors_btn = tk.Button(button_frame, text="scissors", width=10, command=lambda: play("scissors"))
scissors_btn.grid(row=0, column=2, padx=5)
root.mainloop()