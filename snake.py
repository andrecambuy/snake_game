"""Class move snake"""
from turtle import Turtle

MOVE_DISTANCE = 20
START_POSITION = ((0, 0), (0, -20), (0, -40))


class Snake:
    """snake class"""

    def __init__(self):
        self.snake = []
        self.new_snake()
        self.head = self.snake[0]

    def new_snake(self):
        """a new snake"""

        for position in START_POSITION:
            self.add_segment(position)

    def add_segment(self, position):
        """add"""
        new_piece = Turtle('square')
        new_piece.color("white")
        new_piece.pu()
        new_piece.goto(position)
        self.snake.append(new_piece)

    def extend(self):
        """extend"""
        self.add_segment(self.snake[-1].position())

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
