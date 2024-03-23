import time
from turtle import Screen

from snake import Snake
from food import Food
from score_board import Score

screen = Screen()

screen.setup(650, 650)
screen.bgcolor("black")
screen.title('snake game')
screen.tracer(0)

snake = Snake()
food = Food()
points = Score()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.right, "Right")
screen.onkey(snake.left, "Left")

game_true = True
while game_true:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) < 15:
        food.generate_food()
        points.increase_score()
        snake.extend()

    x_axis = snake.head.xcor()
    y_axis = snake.head.ycor()

    if x_axis >= 310 or x_axis <= -310 or y_axis >= 310 or y_axis <= -310:
        points.reset()
        snake.reset()


    for segment in snake.segments[1:]:
        if (snake.head.distance(segment) <= 10):

            points.reset()
            snake.reset()


screen.bgcolor("black")
screen.exitonclick()
