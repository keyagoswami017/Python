# from turtle import Turtle, Screen
import random
import turtle as t


timmy = t.Turtle()
timmy.shape("turtle")
timmy.color("turquoise")

## Draw a square
# for _ in range(4):
#     timmy.forward(100)
#     timmy.left(90)

## Draw a dashed line
# for _ in range(8):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()

## Draw Triangle, square, hectagon, pentagon, hexagon.....
# def draw_shape(num_sides):
#     angle = 360 / num_sides
#     for _ in range(num_sides):
#         timmy.forward(100)
#         timmy.left(angle)
#
# for shape_side in range(3,11):
#     timmy.color(random.choice(["red", "green","pink","purple","brown", "blue","black",]))
#     draw_shape(shape_side)

# # Random Walk
# directions = [0,90,180,270]
# timmy.pensize(10)
# timmy.speed("fastest")
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     random_color = (r,g,b)
#     return random_color
#
# for _ in range(100):
#     #timmy.color(random.choice(["red", "green", "pink", "purple", "brown", "blue", "black", ]))
#     timmy.color(random_color())
#     timmy.forward(30)
#     timmy.setheading(random.choice(directions))


# # Spherical geometry design
# directions = [0,90,180,270]
# timmy.speed("fastest")
# t.colormode(255)
#
# def random_color():
#     r = random.randint(0,255)
#     g = random.randint(0,255)
#     b = random.randint(0,255)
#     r_color = (r,g,b)
#     return r_color
#
# def draw_spirograph(gap):
#     for _ in range(360 // gap):
#         timmy.color(random_color())
#         timmy.circle(100)
#         timmy.setheading(timmy.heading() + gap)
#
# draw_spirograph(10)



screen = t.Screen()
screen.exitonclick()