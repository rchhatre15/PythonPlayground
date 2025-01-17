import json
from tkinter import *
from tkinter import messagebox
import random
import pyperclip
import json
# ---------------------------- PASSWORD GENERATOR ------------------------------- #


def search():
    try:
        with open("password.json", mode="r") as file:
            data = json.load(file)
        messagebox.showinfo(title=f"Info for {web_in.get()}", message=f"Email: {data[web_in.get()]['email']}\n"
                                                                      f"Password: {data[web_in.get()]['password']}")
    except KeyError:
        messagebox.showinfo(title=f"Invalid Website", message=f'There is no data for "{web_in.get()}".')




def generate():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u',
               'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P',
               'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    nr_letters = random.randint(8, 10)
    nr_symbols = random.randint(2, 4)
    nr_numbers = random.randint(2, 4)

    password_list = [random.choice(letters) for _ in range(nr_letters)]
    password_list += [random.choice(symbols) for _ in range(nr_symbols)]
    password_list += [random.choice(numbers) for _ in range(nr_numbers)]

    random.shuffle(password_list)

    val = "".join(password_list)
    pyperclip.copy(val)
    pass_in.insert(END, val)


# ---------------------------- SAVE PASSWORD ------------------------------- #


def add():
    site = web_in.get()
    mail = mail_in.get()
    word = pass_in.get()
    new_data = {
        site: {
            "email": mail,
            "password": word,
        }
    }
    if site.strip() == "" or mail.strip() == "" or word.strip() == "":
        messagebox.showinfo(title="You sold", message="Make sure none of the fields are blank")
    else:
        down = messagebox.askokcancel(title=site, message=f"These are the details entered: \nEmail: {mail}\n"
                                                          f"Password: {word}\nIs it ok to save?")
        if down:
            try:
                with open("password.json", mode="r") as file:
                    data = json.load(file)
                    data.update(new_data)
                    json.dump(data, file, indent=4)
                    # file.write(f"{site} || {mail} || {word}\n")
                    web_in.delete(0, END)
                    pass_in.delete(0, END)
            except FileNotFoundError:
                with open("password.json", mode="w") as file:
                    json.dump(new_data, file, indent=4)
                    # file.write(f"{site} || {mail} || {word}\n")
                    web_in.delete(0, END)
                    pass_in.delete(0, END)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Password Manager")
window.config(padx=50, pady=50, bg="white")

canvas = Canvas(width=200, height=200, bg="white", highlightthickness=0)
img = PhotoImage(file="logo.png")
canvas.create_image(100, 100, image=img)
canvas.grid(column=1, row=0)

website = Label(text="Website:", fg="black", bg="white")
website.grid(column=0, row=1)

email = Label(text="Email/Username:", fg="black", bg="white")
email.grid(column=0, row=2)

password = Label(text="Password:", fg="black", bg="white")
password.grid(column=0, row=3)

web_in = Entry(width=18, highlightthickness=0)
web_in.config(bg="white", fg="black")
web_in.grid(column=1, row=1)
web_in.focus()

search = Button(width=17, text="Search", command=search, highlightbackground="white")
search.grid(column=2, row=1)

mail_in = Entry(width=35, highlightthickness=0)
mail_in.config(bg="white", fg="black")
mail_in.insert(END, "rchhatre15@gmail.com")
mail_in.grid(column=1, row=2, columnspan=2)

pass_in = Entry(width=18, highlightthickness=0)
pass_in.config(bg="white", fg="black")
pass_in.grid(column=1, row=3)

gen = Button(width=17, text="Generate Password", command=generate, highlightbackground="white")
gen.grid(column=2, row=3)

add = Button(text="Add", command=add, highlightbackground="white", width=36)
add.grid(column=1, row=4, columnspan=2)



window.mainloop()

