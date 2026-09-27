import random
from turtle import Turtle, Screen

# timmy = Turtle(shape="turtle")
screen = Screen()

## Moving the turtle
# def move_fwd():
#     timmy.forward(10)
# def move_bwd():
#     timmy.backward(10)
# def move_ccw():
#     timmy.right(10)
# def move_cw():
#     timmy.left(10)
# def clear_screen():
#     timmy.clear()
#     timmy.penup()
#     timmy.home()
#     timmy.pendown()
#
# screen.listen()
# screen.onkey(move_fwd,"w")
# screen.onkey(move_bwd,"s")
# screen.onkey(move_cw,"d")
# screen.onkey(move_ccw,"a")
# screen.onkey(clear_screen,"c")

# Turtle Race
screen.setup(width=500, height=400)
user_bet = screen.textinput("Make you bet","Which turtle will win the race? Enter the color")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
y_pos = [-70,-40,-10,20,50,80]
is_race_on = False
all_turtles = []

for turtle_idx in range(0,6):
    new_turtle = Turtle(shape="turtle")
    new_turtle.penup()
    new_turtle.color(colors[turtle_idx])
    new_turtle.goto(-235,y_pos[turtle_idx])
    all_turtles.append(new_turtle)

if user_bet:
    is_race_on = True

while is_race_on:
        for turtle in all_turtles:
            if turtle.xcor() > 235:
                is_race_on = False
                winner = turtle.pencolor()
                if winner == user_bet:
                    print(f"You win! The {user_bet} turtle wins.")
                else:
                    print(f"You lose! The {winner} turtle wins.")

            random_dist = random.randint(0, 10)
            turtle.forward(random_dist)

screen.exitonclick()