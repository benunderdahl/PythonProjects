from turtle import *
import random


timmy = Turtle()
timmy.shape("turtle")
colors = [
    "SlateBlue",
    "MediumAquamarine",
    "DarkOliveGreen",
    "LightCoral",
    "DeepPink",
    "Turquoise",
    "Goldenrod",
    "Tomato",
    "Orchid",
    "CadetBlue",
    "FireBrick"
]
timmy.width(25)
timmy.speed(10)
directions = [90, 180, 270, 360]

def random_walk():
    timmy.setheading(random.choice(directions))
    timmy.pencolor(random.choice(colors))
    timmy.forward(50)

for _ in range(1000):
    random_walk()

screen = Screen()
screen.exitonclick()










