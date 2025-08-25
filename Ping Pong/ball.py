from turtle import Turtle

class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(0,0)
        self.xmove = 10
        self.ymove = 10
        self.move_speed = 0.1

    def move(self):
        new_y = self.ycor() + self.ymove
        new_x = self.xcor() + self.xmove
        self.goto(new_x, new_y)

    def bounce(self):
        self.ymove *= -1

    def collision(self):
        self.move_speed *= 0.9
        self.xmove *= -1


    def reset(self):
        self.move_speed = 0.1
        self.goto(0,0)