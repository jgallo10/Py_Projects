from turtle import Turtle
FONT = ("Courier", 24, "normal")


class Scoreboard(Turtle):
    
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.level = 0
        self.update_level()
        self.speeding = 0.1
        

    def update_level(self):
        self.clear()
        self.goto(-220, 265)
        self.write("Level: %s" % self.level, align="center", font=FONT)
        
    def level_up(self):
        self.level += 1
        self.update_level()
        self.speeding *= .8
        
        
        