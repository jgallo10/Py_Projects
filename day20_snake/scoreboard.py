from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Arial", 20, "normal")


class Score(Turtle):
    
    def __init__(self):
        super().__init__()
        with open("data.txt") as data_file:
            top_score = data_file.read()
        self.points = 0
        self.highscore = int(top_score)
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
            with open("data.txt", mode="w") as data_file:
                data_file.write(f"{self.highscore}")
        self.points = 0
        self.update_scoreboard() 
    
    '''def game_over(self):
        self.goto(0,0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)'''