import turtle
import random

gamma = turtle.Screen()
beta = turtle.Turtle()
beta.shape("turtle")
beta.speed(0)


d = 10
a = 90

is_in_screen =True

x = random.randrange(0,2)

for i in range(0,2):
    if x == 1:
        print("heads")
    else:
        print("tails")


while is_in_screen:
    x = random.randrange(0,2)
    if x==1:
        beta.right(a)
    else:
        beta.left(a)
    beta.forward(d)

    turtleX = beta.xcor()
    turtleY = beta.ycor()

    x_range = gamma.window_width()/2
    y_range = gamma.window_height()/2

    if abs(turtleX) > x_range or abs(turtleY) > y_range:
        is_in_screen = False




