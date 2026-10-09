# Paddle pong game

from turtle import Screen
from Day22_ClassTask import Paddle, Ball, Scoreboard
import time

HEIGHT = 600
WIDTH = 800


screen = Screen()
screen.bgcolor("black")
screen.setup(width=WIDTH, height=HEIGHT)
screen.title("Pong Game")
screen.tracer(0)


r_paddle = Paddle((350,0))
l_paddle = Paddle((-350,0))
ball = Ball((0,0))
scoreboard = Scoreboard()

screen.listen()
screen.onkey(r_paddle.paddle_up,"Up")
screen.onkey(r_paddle.paddle_down,"Down")
screen.onkey(l_paddle.paddle_up,"w")
screen.onkey(l_paddle.paddle_down,"s")

game_on = True
while game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        # needs to bounce
        ball.bounce_y()

    # Detect collision with the paddle
    if ball.distance(r_paddle) < 50 or ball.xcor() > 320 or ball.distance(l_paddle) < 50 or ball.xcor() < -320:
        ball.bounce_x()

    # Detect R Paddle misses the ball
    if ball.xcor() > 380:
        ball.reset_position()
        scoreboard.l_pointer()

    # Detect L Paddle misses the ball
    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_pointer()


screen.exitonclick()
