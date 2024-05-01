from turtle import Turtle, Screen
import random

tim = Turtle()
tim.shape("turtle")
 
num = 3
colors = ['red', 'black', 'blue', 'green', 'purple', 'magenta', 'orange', 'lime', 'navy', 'plum', 'violet']

while num < 11:
    angle = 360 / num
    tim.color(random.choice(colors))
    for i in range(num):
        tim.forward(100)
        tim.right(angle)
    num += 1

screen = Screen()
screen.exitonclick()