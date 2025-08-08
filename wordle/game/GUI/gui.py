# import my functions and GUI library
from wordle.game.logic import select_word, compare_word
from wordle.game.utils.THE_FETCHING import get_Words

import tkinter as tk

#  get thr true word
Target = select_word()
# the tuple list 
history = []
attempts = 6 

# create my program canvas by root 
root = tk.Tk()
#  title of my program
root.title("WORDLE GAME ")
#  size of my program
root.geometry("500x500")
root.configure(bg="#f0f0f0")

# create a label for input field 
tk.Label(root, text="Enter a 5 letter word", font=("Arial", 14), bg="#f0f0f0", fg="#333").pack(pady=10)

# pack the user input and make it well oriented and centered 
entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)

# test
feedback = tk.Label(root, text="", fg="blue", font=("Arial", 12), bg="#f0f0f0")
feedback.pack(pady=5)

history_box = tk.Text(root, height=10, width=40, font=("Courier", 10), bg="#fff", fg="#333")
history_box.pack(pady=10)

# the submit 
def submit():
    global attempts
    guess = entry.get().lower()
    if len(guess) != 5:
        feedback.config(text="Please enter a 5 letter word")
        return
    if guess not in get_Words():
        feedback.config(text="Please enter a valid word")
        return

    result = compare_word(guess, Target)
    history.append((guess, result))
    history_box.insert(tk.END, f"{guess.upper()} → {result}\n")

    if guess == Target:
        feedback.config(text="BRAVOO \n You win ")
        entry.config(state="disabled")
        submit_button.config(state="disabled")
    else:
        attempts -= 1 
        if attempts == 0:
            feedback.config(text=f"Game Over , You are LOSER \nThe word was: {Target.upper()}")
            entry.config(state="disabled")
            submit_button.config(state="disabled")
        else:
            feedback.config(text=f"Remaining attempts: {attempts}")

# add a restaet button to can guess another word without close 
# restart game
def restart():
    global Target, history, attempts
    Target = select_word()
    history = []
    attempts = 6
    entry.config(state="normal")
    submit_button.config(state="normal")
    entry.delete(0, tk.END)
    feedback.config(text="")
    history_box.delete("1.0", tk.END)

# make a button for submit 
submit_button = tk.Button(root, text="Submit",
                          command=submit,
                          bg="#4CAF50", 
                          fg="white",
                          font=("Arial", 12))
submit_button.pack(pady=5)

# make a button for restart
restart_button = tk.Button(root, text="Restart",
                           command=restart,
                           bg="#2196F3",
                           fg="white",
                           font=("Arial", 12))

restart_button.pack(pady=5)

# 

root.mainloop()
