from tkinter import *
import random
import pandas as pd

#--------------------------------------- CONSTANTS ---------------------------------------#
BACKGROUND_COLOR = "#B1DDC6"

#--------------------------------------- PANDAS ---------------------------------------#
data = pd.read_csv("data/german_words_top_3000.csv")
to_learn = data.to_dict(orient="records")
current_word = {}
to_learn = {}
#--------------------------------------- FUNCTIONS ---------------------------------------#

try:
    data = pd.read_csv("data/words_to_learn.csv")
except FileNotFoundError:
    original_data = pd.read_csv("data/german_words_top_3000.csv")
    to_learn = original_data.to_dict(orient="records")
else:
    to_learn = data.to_dict(orient="records")
    current_card = {}
def next_card():
    global current_word, flip_timer
    window.after_cancel(flip_timer)
    current_word = random.choice(to_learn)
    canvas.itemconfig(card_side, image=card_front)
    canvas.itemconfig(card_title, text="German", fill="black")
    canvas.itemconfig(card_word, text=current_word["german"], fill="black")
    flip_timer = window.after(3000, func=flip_card)

def flip_card():
    canvas.itemconfig(card_side, image=card_back)
    canvas.itemconfig(card_title, text="English", fill="white")
    canvas.itemconfig(card_word, text=current_word["english"], fill="white")

def known():
    to_learn.remove(current_word)
    df = pd.DataFrame(to_learn)
    df.to_csv("data/words_to_learn.csv", index=False)
    print(len(to_learn))
    next_card()
#--------------------------------------- UI ---------------------------------------#

window = Tk()
window.title("Flash Me")
window.config(bg=BACKGROUND_COLOR, padx=50, pady=50)

flip_timer = window.after(3000, flip_card)
# images
card_front = PhotoImage(file="images/card_front.png")
card_back = PhotoImage(file="images/card_back.png")
wrong = PhotoImage(file="images/wrong.png")
correct = PhotoImage(file="images/right.png")

canvas = Canvas(window, width=800, height=526)
canvas.config(bg=BACKGROUND_COLOR, highlightthickness=0)
card_side = canvas.create_image(400, 263, image=card_front)
card_title = canvas.create_text(400, 150, text="", font=("Arial", 40, "italic"))
card_word = canvas.create_text(400, 263, text="", font=("Arial", 48, "bold"))
canvas.grid(row=0, column=0, columnspan=2)


#--------------------------------------- BUTTONS ---------------------------------------#

wrong_button = Button(image=wrong, highlightthickness=0, command=next_card)
wrong_button.grid(row=1, column=0)

correct_button = Button(image=correct, highlightthickness=0, command=known)
correct_button.grid(row=1, column=1)

next_card()
window.mainloop()