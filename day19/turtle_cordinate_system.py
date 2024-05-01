from turtle import Turtle, Screen
import random

is_race_on = False
screen = Screen()
screen.setup(width=500, height=400)
user_bets = screen.textinput(title="Make your bet", prompt="Which turtle will win the rece? Enter your color: ")
colors =["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

y = 60
for turtle_index in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.penup()
    new_turtle.goto(x=-230, y=y)
    y -= 25
    all_turtles.append(new_turtle)

if user_bets:
    is_race_on = True
    
while is_race_on: 
    
    for turtle in all_turtles:
        if turtle.xcor() > 230:
            winning_turtle = turtle.pencolor()
            is_race_on = False
            if winning_turtle == user_bets:
                print(f"You've won! The {winning_turtle} turtle is the winner!")
            else:
                print(f"Sorry you lost! The {winning_turtle} turtle is the winner!")
        rand_distance = random.randint(0,10)
        turtle.forward(rand_distance)


screen.exitonclick() 