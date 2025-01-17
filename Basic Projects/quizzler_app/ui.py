from tkinter import *
from quiz_brain import QuizBrain

THEME_COLOR = "#375362"


class QuizInterface:
    def __init__(self, quiz: QuizBrain):
        self.quiz_brain = quiz

        self.window = Tk()
        self.window.title("Quizzler")
        self.window.config(padx=20, pady=20, bg=THEME_COLOR)

        self.score_l = Label(self.window, text=f"Score: {self.quiz_brain.score}", font=("Arial", 20, "italic"),
                             bg=THEME_COLOR, fg="white")
        self.score_l.grid(row=0, column=1)

        self.canvas = Canvas(height=250, width=300, bg="white")
        self.question_text = self.canvas.create_text(
            150,
            125,
            width=280,
            font=("Arial", 20, "italic"),
            text="This is a true or false question focus up",
            fill=THEME_COLOR)
        self.canvas.grid(column=0, row=1, columnspan=2, padx=50, pady=50)

        false_image = PhotoImage(file="images/false.png")
        self.false = Button(image=false_image, highlightthickness=0, command=self.false_press)
        self.false.grid(row=2, column=1)

        true_image = PhotoImage(file="images/true.png")
        self.true = Button(image=true_image, highlightthickness=0, command=self.true_press)
        self.true.grid(row=2, column=0)

        self.get_next_question()

        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz_brain.still_has_questions():
            self.score_l.config(text=f"Score: {self.quiz_brain.score}")
            temp_text = self.quiz_brain.next_question()
            self.canvas.itemconfig(self.question_text, text=temp_text)
        else:
            self.canvas.itemconfig(self.question_text, text="You have completed the quiz")
            self.true.config(state="disabled")
            self.false.config(state="disabled")

    def false_press(self):
        if self.quiz_brain.check_answer("False"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)

    def true_press(self):
        if self.quiz_brain.check_answer("True"):
            self.canvas.config(bg="green")
        else:
            self.canvas.config(bg="red")

        self.window.after(1000, self.get_next_question)




