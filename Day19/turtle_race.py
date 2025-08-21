from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=1050, height=1000)
choice = screen.textinput(title="Choose your legend", prompt="red, orange, yellow, green, blue, indigo, violet :)").lower()
y = [300, 200, 100, 0, -100, -200, -300]
colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]
race_time = False
all_turtles = []

for i in range(len(colors)):
    new_turtle = Turtle(shape="turtle")
    new_turtle.speed("fastest")
    new_turtle.color(colors[i])
    new_turtle.penup()
    new_turtle.goto(x=-500, y=y[i])
    all_turtles.append(new_turtle)

if choice:
    race_time = True

while race_time:
    for turtle in all_turtles:
        if turtle.xcor() > 450:
            winner = turtle.pencolor()
            if winner == choice:
                print("You Won, Congratulations!")
            else:
                print("You Lost, better luck next time :*(")
            race_time = False
        distance = random.randint(0, 10)
        turtle.forward(distance)

screen.exitonclick()