import turtle as turt
import random


turt.colormode(255)
tim = turt.Turtle()
tim.shape("turtle")
tim.width(4)
tim.speed(10)


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r,g,b)
    return rand_color



for _ in range(250):
    tim.color(random_color())
    tim.circle(100)
    tim.right(10)





screen = turt.Screen()
screen.exitonclick()