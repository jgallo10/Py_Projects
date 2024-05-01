import turtle as T
import random

T.colormode(255)
tim = T.Turtle()
T.speed("fastest")

num = 0


def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    rand_color = (r,g,b)
    return rand_color


while num < 70:
    tim.color(random_color())
    tim.circle(90)
    tim.right(5)
    num += 1
    print(num)
    
    
    
    
screen = T.Screen()
screen.exitonclick()
