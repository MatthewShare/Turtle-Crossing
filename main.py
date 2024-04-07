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
screen.onkey(player.move, "Up")
car = CarManager()
scoreboard = Scoreboard()


game_is_on = True
number_of_steps = 0
dividing_number = 6
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.move()
    number_of_steps += 1
    if player.ycor() > 280:
        player.restart()
        car.level_up()
        scoreboard.level_up_score()
        if dividing_number > 1:
            dividing_number -= 1
    if number_of_steps % dividing_number == 0:
        car.create_car()
    for each_car in car.cars:
        if each_car.distance(player) < 25:
            game_is_on = False
            scoreboard.game_over()




screen.exitonclick()

