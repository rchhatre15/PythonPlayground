from tkinter import *
# ---------------------------- CONSTANTS ------------------------------- #
PINK = "#e2979c"
RED = "#e7305b"
GREEN = "#9bdeac"
YELLOW = "#f7f5dd"
FONT_NAME = "Courier"
WORK_MIN = 25
SHORT_BREAK_MIN = 5
LONG_BREAK_MIN = 20
reps = 1
on = False
checks = "✔"

# ---------------------------- TIMER RESET ------------------------------- # 


def reset():
    global reps
    global on
    global checks
    on = False
    reps = 1
    checks = "✔"
    canvas.itemconfig(text, text="00:00")
    label.config(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
    check_mark.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "normal"))


# ---------------------------- TIMER MECHANISM ------------------------------- # 


def start():
    global on
    on = True
    label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
    countdown(WORK_MIN, 0)


# ---------------------------- COUNTDOWN MECHANISM ------------------------------- # 


def countdown(min_count, sec_count):
    if on:
        if min_count > 9 and sec_count > 9:
            canvas.itemconfig(text, text=f"{min_count}:{sec_count}")
        elif min_count < 10 and sec_count < 10:
            canvas.itemconfig(text, text=f"0{min_count}:0{sec_count}")
        elif min_count < 10:
            canvas.itemconfig(text, text=f"0{min_count}:{sec_count}")
        else:
            canvas.itemconfig(text, text=f"{min_count}:0{sec_count}")

        if sec_count == 0 and min_count == 0:
            global reps
            global checks
            reps += 1
            if not reps % 2 == 0:
                countdown(WORK_MIN, 0)
                label.config(text="Work", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
            elif reps % 8 == 0:
                countdown(LONG_BREAK_MIN, 0)
                label.config(text="Break", fg=PINK, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
                if checks == "✔✔✔✔":
                    check_mark.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "normal"))
                    checks = "✔"
                else:
                    check_mark.config(text=checks, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "normal"))
                    checks += "✔"

            else:
                countdown(SHORT_BREAK_MIN, 0)
                label.config(text="Break", fg=RED, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
                if checks == "✔✔✔✔✔":
                    check_mark.config(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "normal"))
                    checks = "✔"
                else:
                    check_mark.config(text=checks, fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "normal"))
                    checks += "✔"

        elif sec_count > 0:
            window.after(1000, countdown, min_count, sec_count - 1)
        else:
            window.after(1000, countdown, min_count - 1, 59)


# ---------------------------- UI SETUP ------------------------------- #
window = Tk()
window.title("Pomodoro")
window.config(padx=100, pady=50, bg=YELLOW)

label = Label(text="Timer", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 35, "normal"))
label.grid(column=1, row=0)

canvas = Canvas(width=200, height=223, bg=YELLOW, highlightthickness=0)
img = PhotoImage(file="tomato.png")
canvas.create_image(100, 112, image=img)
text = canvas.create_text(100, 135, text="25:00", fill="white", font=(FONT_NAME, 35, "bold"))
canvas.grid(column=1, row=1)

start = Button(text="start", command=start, highlightbackground=YELLOW)
start.grid(column=0, row=2)

check_mark = Label(text="", fg=GREEN, bg=YELLOW, font=(FONT_NAME, 30, "normal"))
check_mark.grid(column=1, row=3)

reset = Button(text="reset", command=reset, highlightbackground=YELLOW)
reset.grid(column=2, row=2)

window.mainloop()
