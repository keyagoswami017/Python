# Snake Game connected to Day20
from turtle import Turtle
import random
START_POS = [(0,0), (-20,0), (-40,0)]
MOVE_SPEED = 20
DIRECTIONS = [0,90,180,270]
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0
ALIGN = "center"
FONT = ("Verdana", 20, "normal")

class Snake:
    def __init__(self):
        self.turtles = []
        self.create_snake()
        self.head = self.turtles[0]

    def create_snake(self):
        for i in START_POS:
            self.add_snake(i)

    def add_snake(self,position):
        t = Turtle(shape="square")
        t.color("white")
        t.penup()
        t.goto(position)
        self.turtles.append(t)

    def extend_snake(self):
        self.add_snake(self.turtles[-1].position())


    def move(self):
        for t_num in range(len(self.turtles) - 1, 0, -1):
            new_x = self.turtles[t_num - 1].xcor()
            new_y = self.turtles[t_num - 1].ycor()
            self.turtles[t_num].goto(new_x, new_y)
        self.head.forward(MOVE_SPEED)

    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

class Food(Turtle):

    def __init__(self):
        super().__init__()
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=0.5, stretch_len=0.5)
        self.fillcolor("blue")
        self.speed("fastest")
        self.refresh()

    def refresh(self):
        random_x = random.randint(-280, 280)
        random_y = random.randint(-280, 280)
        self.goto(random_x, random_y)

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update()

    def update(self):
        self.write(f"Score: {self.score}", align = ALIGN, font = FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update()

    def game_over(self):
        self.color("red")
        self.goto(0, 0)
        self.write("Game Over", align = ALIGN, font = FONT)

