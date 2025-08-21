from turtle import Turtle, Screen


turt = Turtle()
screen = Screen()
angle = 0
turt.shape("turtle")
turt.width(10)

def move_up():
    turt.setheading()
def move_back():
    turt.back(10)
def move_left():
    global angle
    angle += 5
    turt.setheading(angle)
def move_right():
    global angle
    angle -= 5
    turt.setheading(angle)
def move_forward():
    turt.forward(10)

screen.listen()

screen.onkeypress(key="Down", fun=move_back)
screen.onkeypress(key="Left", fun=move_left)
screen.onkeypress(key="Right", fun=move_right)
screen.onkeypress(key="Up", fun=move_forward)
screen.exitonclick()