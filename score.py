"""SCORE"""

from turtle import Turtle


class Scoreboard(Turtle):

    """Score in the game"""

    def __init__(self):

        super().__init__()

        self.score = 0
        self.hideturtle()
        self.color("white")
        self.pu()
        self.goto(0, 280)
        self.write(f"Score: {self.score}", align="center",
                   font=('Arial', 12, 'normal'))

    def increase_socre(self):
        """pointer"""
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align="center",
                   font=('Arial', 12, 'normal'))

    def game_over(self):
        """game over"""
        self.goto(0, 0)
        self.write("GAME OVER", align="center",
                   font=('Arial', 12, 'normal'))
