"""Class move snake"""
from turtle import Turtle

MOVE_DISTANCE = 20


class Snake:
    """snake class"""

    def __init__(self):
        self.snake = []
        self.new_snake()
        self.head = self.snake[0]

    def new_snake(self):
        """a new snake"""

        for i in range(0, 3):
            new_piece = Turtle('square')
            new_piece.color("white")
            new_piece.pu()
            x_move = i * -MOVE_DISTANCE
            new_piece.goto(x=x_move, y=0)
            self.snake.append(new_piece)

    def move(self):
        """move snake"""
        for seg_num in range((len(self.snake) - 1), 0, -1):
            self.snake[seg_num].goto(x=self.snake[seg_num - 1].xcor(),
                                     y=self.snake[seg_num - 1].ycor())
        self.head.fd(MOVE_DISTANCE)

    def go_up(self):
        """up"""
        if self.head.heading() != 270:
            self.head.seth(90)

    def go_down(self):
        """down"""
        if self.head.heading() != 90:
            self.head.seth(270)

    def go_left(self):
        """left"""
        if self.head.heading() != 0:
            self.head.seth(180)

    def go_right(self):
        """right"""
        if self.head.heading() != 180:
            self.head.seth(0)
