

# for emojis as same as thr trial file style 
from PIL import Image, ImageDraw, ImageFont, ImageTk
import tkinter as tk
from wordle.game.logic import select_word, compare_word
from wordle.game.utils.THE_FETCHING import get_Words

# Function to create emoji image
def emoji_img(size, text):
    font = ImageFont.truetype("seguiemj.ttf", size=int(round(size*72/96, 0))) 
    im = Image.new("RGBA", (size, size), (255, 255, 255, 0))
    draw = ImageDraw.Draw(im)
    draw.text((size/2, size/2), text, embedded_color=True, font=font, anchor="mm")
    return ImageTk.PhotoImage(im)

Target = select_word()
history = []
attempts = 6

root = tk.Tk()
root.title("WORDLE GAME ")
root.geometry("500x500")
root.configure(bg="#f0f0f0")

tk.Label(root, text="Enter a 5 letter word", font=("Arial", 14), bg="#f0f0f0", fg="#333").pack(pady=10)
entry = tk.Entry(root, font=("Arial", 12), justify="center")
entry.pack(pady=5)
feedback = tk.Label(root, text="", fg="blue", font=("Arial", 12), bg="#f0f0f0")
feedback.pack(pady=5)

history_frame = tk.Frame(root, bg="#f0f0f0")
history_frame.pack(pady=10)

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

    row_frame = tk.Frame(history_frame, bg="#f0f0f0")
    tk.Label(row_frame, text=guess.upper(), font=("Arial", 12), bg="#f0f0f0").pack(side="left", padx=5)
    for symbol in result:
        img = emoji_img(30, symbol)
        lbl = tk.Label(row_frame, image=img, bg="#f0f0f0")
        lbl.image = img  
        lbl.pack(side="left", padx=2)
        row_frame.pack(anchor="w")

    if guess == Target:
        feedback.config(text="BRAVOO \nYou win")
        entry.config(state="disabled")
        submit_button.config(state="disabled")
    else:
        attempts -= 1
        if attempts == 0:
            feedback.config(text=f"Game Over \n , you are LOSER , \n  The word was: {Target.upper()}")
            entry.config(state="disabled")
            submit_button.config(state="disabled")
        else:
            feedback.config(text=f"Remaining attempts: {attempts}")
# add restart button to make another guess in same game 
def restart():
    global Target, history, attempts
    Target = select_word()
    history = []
    attempts = 6
    entry.config(state="normal")
    submit_button.config(state="normal")
    entry.delete(0, tk.END)
    feedback.config(text="")
    for widget in history_frame.winfo_children():
     widget.destroy()
# /////////////////////////////////////////////////////////////////
#///////////////////////// buttin styles ////////////////////////////
submit_button = tk.Button(root, text="Submit", command=submit, bg="#4CAF50", fg="white", font=("Arial", 12))
submit_button.pack(pady=5)

restart_button = tk.Button(root, text="Restart", command=restart, bg="#2196F3", fg="white", font=("Arial", 12))
restart_button.pack(pady=5)

root.mainloop()
