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
        with open("save.txt") as file:
            self.high_score = int(file.read())
        self.update_score()



    def display_score(self):
            self.write(f"Score: {self.score} ", align="center", font=("Arial", 24, "normal"))

    def update_score(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
        self.write(f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=GAME_FONT)

    def game_over(self):
        self.goto(0,0)
        self.write("Game Over", align=ALIGNMENT, font=GAME_OVER_FONT)

    def reset(self):
        with open("save.txt", "w") as file:
            file.write(f"{str(self.high_score)}")
        self.score = 0
        self.update_score()

    def increase_score(self):
        self.score += 1
        self.update_score()