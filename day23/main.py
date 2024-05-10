import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
car = CarManager()
level = Scoreboard()

screen.listen()
screen.onkeypress(player.move_up, "Up")


game_is_on = True
num = 0
frequancy = 6
while game_is_on:
    time.sleep(level.speeding)
    screen.update()
    
    if num % frequancy == 0:
        car.add_car()
    num += 1
    car.drive()
    
    if player.ycor() > 280:
        level.level_up()
        player.reset_position()
        if level.level % 2 == 0:
            frequancy -= 1
        
    for driver in car.traffic:
        if player.distance(driver) < 20:
            game_is_on = False
    
screen.exitonclick()
