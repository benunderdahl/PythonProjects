import colorgram
import turtle as t
import random

colors = colorgram.extract("hirst.jpg", 30)
rgb = []

for color in colors:
    r = color.rgb.r
    g = color.rgb.g
    b = color.rgb.b
    rgb.append((r, g, b))

t.colormode(255)
timmy = t.Turtle()
timmy.hideturtle()
timmy.color("green")
timmy.speed("fastest")
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)

for dots in range (1, 100 + 1):
    timmy.dot(20,random.choice(rgb))
    timmy.forward(50)
    if dots % 10 == 0:
        timmy.setheading(90)
        timmy.forward(50)
        timmy.setheading(180)
        timmy.forward(500)
        timmy.setheading(0)