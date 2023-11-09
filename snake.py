from turtle import Turtle

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
move_distance = 20
up = 90
down = 270
left = 180
right = 0


class Snake:

    def __init__(self):
        self.body = []
        self.create_snake()
        self.head = self.body[0]

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.snake_block(position)

    def snake_block(self, position):
        snake_part = Turtle(shape="square")
        snake_part.penup()
        snake_part.fillcolor("green")
        snake_part.pencolor("green")
        snake_part.goto(position)
        self.body.append(snake_part)

    def extend_tail(self):
        self.snake_block(self.body[-1].position())

    def reset(self):
        for parts in self.body:
            parts.goto(1000,1000)
        self.body.clear()
        self.create_snake()
        self.head = self.body[0]

    def move_snake(self):
        for i, move_body_part in reversed(list(enumerate(self.body))):
            if move_body_part is not self.body[0]:
                move_body_part.goto(self.body[i - 1].pos())
            else:
                move_body_part.forward(move_distance)

    def up(self):
        if self.head.heading() != down:
            self.head.setheading(up)

    def down(self):
        if self.head.heading() != up:
            self.head.setheading(down)

    def left(self):
        if self.head.heading() != right:
            self.head.setheading(left)

    def right(self):
        if self.head.heading() != left:
            self.head.setheading(right)
