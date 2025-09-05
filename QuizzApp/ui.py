from tkinter import *
from quiz_brain import QuizBrain



THEME_COLOR = "#375362"
FONT = ("Arial", 20, "italic")

class UserInterface:

    def __init__(self, quiz_brain: QuizBrain):
        self.quiz = quiz_brain
        self.window = Tk()
        self.window.title("Quiz Wiz")
        self.window.config(bg=THEME_COLOR, padx=20, pady=20)
        self.score = 0
        self.score_label = Label(bg=THEME_COLOR, fg="white", text="Score: 0", font=("Ariel", 10, "bold"))
        self.score_label.grid(row=0, column=1, pady=(0, 20))
        self.canvas = Canvas(self.window, width=300, height=250)
        self.canvas_text = self.canvas.create_text(150, 125, font=FONT, text="Hello, World!", width=280)
        self.canvas.grid(row=1, column=0, columnspan=2, pady=50)
        true_photo = PhotoImage(file="./images/true.png")
        false_photo = PhotoImage(file="./images/false.png")
        self.correct = Button(self.window, image=true_photo, highlightthickness=0, bg=THEME_COLOR, command=self.true_pressed)
        self.false = Button(self.window, image=false_photo, highlightthickness=0, bg=THEME_COLOR, command=self.false_pressed)
        self.correct.grid(row=2, column=0)
        self.false.grid(row=2, column=1)
        self.get_next_question()
        self.window.mainloop()

    def get_next_question(self):
        self.canvas.config(bg="white")
        if self.quiz.still_has_questions():
            self.score_label.config(text=f"Score: {self.score}")
            q_text = self.quiz.next_question()
            self.canvas.itemconfig(self.canvas_text, text=q_text)
        else:
            self.canvas.itemconfig(self.canvas_text, text="End of Quiz")
            self.correct.config(state="disabled")
            self.false.config(state="disabled")

    def true_pressed(self):
        self.get_feedback(self.quiz.check_answer("True"))

    def false_pressed(self):
        self.get_feedback(self.quiz.check_answer("False"))

    def get_feedback(self, is_right):
        if is_right:
            self.canvas.config(bg="green")
            self.score += 1
        else:
            self.canvas.config(bg="red")
        self.window.after(1000, self.get_next_question)