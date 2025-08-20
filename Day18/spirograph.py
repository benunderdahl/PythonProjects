import random
import turtle as t

timmy = t.Turtle()
t.colormode(255)
timmy.speed("fastest")
timmy.shape("turtle")

gap = 5

def random_color() -> tuple:
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    return (r, g, b)

def spirograph(gap):
    timmy.color(random_color())
    timmy.circle(100)
    timmy.setheading(gap)

for _ in range(int(360/gap)):
    spirograph(gap)
    gap += 5




screen = t.Screen()
screen.exitonclick()