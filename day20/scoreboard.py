from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.points = 0
        self.penup 
        self.setpos(0,270)
        self.color("white")
        self.write(f"Score: {self.points}" , False, "center", ("Arial", 20))
        self.hideturtle()
       
        
        
        
    def increaseScore(self):
        self.points = self.points + 1
        self.clear()
        self.write(f"Score: {self.points}" , False, "center", ("Arial", 20))
     
    
    def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)