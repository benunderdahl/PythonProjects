from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 1
        self.goto(0, 280)
        self.update_score()

    def update_score(self):
        global FONT
        self.score += 1
        self.write(f"Level: {self.level}", align="left", FONT)
