"""main File"""
import time
from turtle import Screen
from snake import Snake
from food import Food
from score import Scoreboard

GAME_IS_ON = True

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor('black')
screen.title("My Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
score = Scoreboard()

screen.listen()
screen.onkey(snake.go_up, "Up")
screen.onkey(snake.go_down, "Down")
screen.onkey(snake.go_left, "Left")
screen.onkey(snake.go_right, "Right")

while GAME_IS_ON:
    screen.update()
    time.sleep(0.08)

    snake.move()

    # Detect colision
    if snake.head.distance(food) < 15:
        food.refresh()
        score.increase_socre()
        snake.extend()

    # Detect wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        GAME_IS_ON = False
        score.game_over()

    # Detect body
    for segment in snake.snake[1:]:
        if snake.head.distance(segment) < 10:
            GAME_IS_ON = False
            score.game_over()


screen.exitonclick()
