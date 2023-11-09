import time
from turtle import Screen
from food import Food
from snake import Snake
from scoreboard import ScoreBoard

is_playing = True
my_screen = Screen()
my_screen.tracer(0)
my_screen.bgcolor("black")
my_screen.setup(width=600, height=600)
my_screen.title("Snake Game")

new_snake = Snake()
new_food = Food()
new_scoreboard = ScoreBoard()
my_screen.listen()
my_screen.onkey(new_snake.up, "Up")
my_screen.onkey(new_snake.down, "Down")
my_screen.onkey(new_snake.left, "Left")
my_screen.onkey(new_snake.right, "Right")

while is_playing:
    my_screen.update()
    time.sleep(0.05)
    new_snake.move_snake()

    # Collision with food
    if new_snake.head.distance(new_food) < 15:
        new_scoreboard.increase_score()
        new_food.refresh()
        new_snake.extend_tail()
    # Collision with wall
    if new_snake.head.xcor() > 285 or new_snake.head.xcor() < -285 or new_snake.head.ycor() > 285 or new_snake.head.ycor() < -285:
        new_scoreboard.reset()
        new_snake.reset()

    # Collision with tail
    for segments in new_snake.body[1:]:
        if new_snake.head.distance(segments) < 15:
            new_scoreboard.reset()
            new_snake.reset()
my_screen.exitonclick()
