import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.listen()

player = Player()
score = Scoreboard()
cars = CarManager()

screen.onkey(player.move, "Up")

game_is_on = True
while game_is_on:
    cars.create_car()
    cars.move_cars()
    if player.ycor() > 280:
        score.update_score()
        cars.increase_speed()
        player.reset()

    for car in cars.all_cars:
        if player.distance(car) < 25:
            score.game_over()
            game_is_on = False


    time.sleep(0.1)
    screen.update()

screen.exitonclick()