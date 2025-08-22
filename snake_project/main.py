from turtle import Screen
from snake import Snake
import time

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Legend")
screen.tracer(0)
game = True

snake = Snake()
screen.listen()

while game:
    screen.update()
    time.sleep(0.1)
    snake.move()
    screen.onkeypress(snake.up, "Up")
    screen.onkeypress(snake.down, "Down")
    screen.onkeypress(snake.left, "Left")
    screen.onkeypress(snake.right, "Right")


screen.exitonclick()