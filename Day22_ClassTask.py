from turtle import Turtle

WIDTH, LEN = 5, 1
COUNTER = 20


class Paddle(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=WIDTH, stretch_len=LEN)
        self.penup()
        self.goto(position)

    def paddle_up(self):
        new_y = self.ycor() + COUNTER
        self.goto(self.xcor(), new_y)


    def paddle_down(self):
        new_y = self.ycor() - COUNTER
        self.goto(self.xcor(), new_y)

class Ball(Turtle):
    def __init__(self, position):
        super().__init__()
        self.shape("circle")
        self.color("white")
        self.penup()
        self.goto(position)
        self.x = 10
        self.y = 10
        self.move_speed = 0.1

    def move(self):
        new_x = self.xcor() + self.x
        new_y = self.ycor() + self.y
        self.goto(new_x, new_y)

    def bounce_y(self):
        self.y *= -1

    def bounce_x(self):
        self.x *= -1
        self.move_speed *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.move_speed = 0.1
        self.bounce_x()

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.l_score = 0
        self.r_score = 0
        self.update_score()

    def update_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.l_score, align="center", font=("Arial", 20, "normal"))
        self.goto(100, 200)
        self.write(self.r_score, align="center", font=("Arial", 20, "normal"))

    def l_pointer(self):
        self.l_score += 1
        self.update_score()

    def r_pointer(self):
        self.r_score += 1
        self.update_score()