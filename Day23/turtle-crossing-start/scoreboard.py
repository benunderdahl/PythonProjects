from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.penup()
        self.level = 0
        self.hideturtle()
        self.goto(-210, 260)
        self.update_score()

    def update_score(self):
        self.level += 1
        self.clear()
        self.write(f"Level: {self.level}", align="center", font=FONT)

    def game_over(self):
        self.clear()
        self.goto(0,0)
        self.write("Game Over", align="center", font=FONT)