from turtle import Turtle
ALIGNMENT = "center"
GAME_FONT = ("Arial", 24, "normal")
GAME_OVER_FONT = ("Arial", 50, "normal")

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.display_score()


    def display_score(self):
            self.write(f"Score: {self.score} ", align="center", font=("Arial", 24, "normal"))

    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score} ", align=ALIGNMENT, font=GAME_FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=GAME_OVER_FONT)