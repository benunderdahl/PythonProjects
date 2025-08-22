from turtle import Turtle, Screen

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Legend")
screen.tracer(0)


positions = [(0, 0), (-20,0), (-40,0)]
segments = []
game = True

for position in positions:
    new_segment = Turtle("square")
    new_segment.color("white")
    new_segment.penup()
    new_segment.goto(position)
    segments.append(new_segment)

while game:
    for segment in segments:
        segment.forward(10)



screen.exitonclick()