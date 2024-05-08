from turtle import Turtle, Screen
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard
import time


screen = Screen()


screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

right_pad = Paddle((350, 0))
left_pad = Paddle((-350, 0))
ball = Ball()
score = Scoreboard()

screen.listen()
screen.onkeypress(right_pad.go_up, "Up")
screen.onkeypress(right_pad.go_down, "Down")
screen.onkeypress(left_pad.go_up, "w")
screen.onkeypress(left_pad.go_down, "s")

game_is_on = True
while game_is_on:
        time.sleep(ball.movement)
        screen.update()
        ball.move()
        
        #Detct collison with wall
        if ball.ycor() > 285 or ball.ycor() < -285:
                ball.bounce_y()
                
        #Detct collision with paddle
        if ball.distance(right_pad) < 60 and ball.xcor() > 320 or ball.distance(left_pad) < 60 and ball.xcor() < -320:
                ball.bounce_x()
        
        if ball.xcor() > 370:  
                ball.reset_position()
                score.l_point()
        
        if ball.xcor() < -370:
                ball.reset_position()
                score.r_point()
                
screen.exitonclick()
