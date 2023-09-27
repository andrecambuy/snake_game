"""main File"""
import time
from turtle import Screen
from snake import Snake

GAME_IS_ON = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

while GAME_IS_ON:
    screen.update()
    time.sleep(0.1)

    snake.move()


screen.exitonclick()
