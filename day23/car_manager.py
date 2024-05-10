import random
from turtle import Turtle

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager():
    
    def __init__(self):
        self.traffic = []
        self.add_car()
        
        
    def add_car(self):
        new_car = Turtle("square")
        new_car.color(random.choice(COLORS))
        new_car.shapesize(stretch_wid= 1, stretch_len= 2)
        new_car.penup()
        new_car.left(180)
        new_car.goto(310,random.randrange(-250,250,20))
        self.traffic.append(new_car)
        
        
    def drive(self): 
        for car in range(len(self.traffic)):
            self.traffic[car].forward(MOVE_INCREMENT)
            