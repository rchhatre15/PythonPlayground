from tkinter import *
from random import *
import pandas
BACKGROUND_COLOR = "#B1DDC6"

window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg=BACKGROUND_COLOR)

question = ""
store = 1


def display():
    global question, store
    if len(list(words.keys())) == 0:
        window.after_cancel(store)
    else:
        question = choice(list(words.keys()))
        canvas.itemconfig(img, image=front_img)
        canvas.itemconfig(word, text=question, fill="black")
        canvas.itemconfig(language, text="French", fill="black")
        store = window.after(3000, flip)


def flip():
    global question
    canvas.itemconfig(img, image=back_img)
    canvas.itemconfig(language, text="English", fill="white")
    try:
        canvas.itemconfig(word, text=words[question], fill="white")
    except KeyError:
        canvas.itemconfig(word, text="Set Memorized!", fill="red")


def right():
    global question
    try:
        del words[question]
    except KeyError:
        canvas.itemconfig(word, text="Set Memorized!", fill="red")
    else:
        display()


def wrong():
    try:
        display()
    except KeyError:
        canvas.itemconfig(word, text="Set Memorized!", fill="red")


canvas = Canvas(width=800, height=526, highlightthickness=0, bg=BACKGROUND_COLOR)
front_img = PhotoImage(file="images/card_front.png")
back_img = PhotoImage(file="images/card_back.png")
img = canvas.create_image(400, 263, image=front_img)
language = canvas.create_text(400, 150, text="French", fill="black", font=("ariel", 40, "italic"))
word = canvas.create_text(400, 263, text="Word", fill="black", font=("ariel", 60, "bold"))
canvas.grid(column=0, row=0, columnspan=2)

wrong_image = PhotoImage(file="images/wrong.png")
wrong = Button(image=wrong_image, highlightthickness=0, command=wrong)
wrong.grid(row=1, column=0)

right_image = PhotoImage(file="images/right.png")
right = Button(image=right_image, highlightthickness=0, command=right)
right.grid(row=1, column=1)

data = pandas.read_csv("data/french_words.csv")
words = dict(zip(data.French, data.English))
print(words)

display()

window.mainloop()
