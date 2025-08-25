from turtle import Screen
from paddle import Paddle
from ball import Ball
from score import Score
import time

game = True
screen = Screen()
screen.bgcolor("black")
screen.setup(width=800, height=600)
screen.title("Pong")
screen.listen()
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350, 0))
ball = Ball()
score = Score()

screen.onkey(r_paddle.up, "Up")
screen.onkey(r_paddle.down, "Down")
screen.onkey(l_paddle.up, "w")
screen.onkey(l_paddle.down, "s")


while game:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
    elif ball.distance(r_paddle) < 50 and ball.xcor() > 320 or ball.distance(l_paddle) < 50 and ball.xcor() < -320:
        ball.collision()
    if ball.xcor() > 380:
        ball.reset()
        score.l_point()
    if ball.xcor() < -380:
        score.r_point()
        ball.reset()


screen.exitonclick()