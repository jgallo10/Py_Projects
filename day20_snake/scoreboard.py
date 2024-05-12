from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        self.points = 0
        self.highscore = 0
        self.penup 
        self.setpos(0,270)
        self.color("white")
        self.hideturtle()
        self.update_scoreboard()
        
    def update_scoreboard(self):
        self.clear()
        self.write(f"Score: {self.points} High Score: {self.highscore}" , False, "center", ("Arial", 20))
        
        
    def increaseScore(self):
        self.points = self.points + 1
        self.update_scoreboard()
     
    
    
    def reset(self):
        if self.points > self.highscore:
            self.highscore = self.points
        self.points = 0
        self.update_scoreboard() 
    
    '''def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)'''