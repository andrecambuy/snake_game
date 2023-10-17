"""SCORE"""

from turtle import Turtle


#create file and read him
with open("data.txt", mode="w") as f:
    f.write("0")
with open("data.txt", mode="r") as f:
    hightscore_file = f.read()

class Scoreboard(Turtle):

    """Score in the game"""

    def __init__(self):

        super().__init__()

        self.score = 0
        self.hightscore = hightscore_file
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(0, 280)
        self.update_scoreborad()

    def update_scoreborad(self):
        self.clear()
        self.write(f"Score: {self.score} Hight Score {self.hightscore}" , align="center",
                   font=('Arial', 12, 'normal'))

    def increase_socre(self):
        """pointer"""
        self.score += 1
        self.update_scoreborad()


    def reset(self):
        if self.score > int(self.hightscore):
            self.hightscore = self.score
            with open("data.txt", mode="w") as data:
                data.write(f"{str(self.hightscore)}")
        self.score = 0
        self.update_scoreborad()

