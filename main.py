from turtle import Screen
import time as t
from snake import Snake
from food import Food
from scoreboard import ScoreBoard

# Creating Objects
screen = Screen()
food = Food()
scoreboard = ScoreBoard()

screen.title("The Snake")
screen.bgcolor("black")
screen.setup(width=600, height=600)
screen.tracer(0)

snake = Snake()
screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(snake.down, "Down")

game_is_on = True
while game_is_on:
    screen.update()
    t.sleep(0.1)
    snake.move()

    # Detecting collision with food
    if snake.head.distance(food) < 15:
        food.refresh()
        snake.extent()
        scoreboard.increase_score()

    # Detecting collision with wall
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        snake.reset()
        snake.segments = []
        snake.create_snake()
        scoreboard.reset()


    # Detecting collision with tail
    for segment in snake.segments[1:]:
        if snake.head.distance(segment) < 10:
            continue

screen.exitonclick()
