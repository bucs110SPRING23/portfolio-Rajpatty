import turtle
import random

right = 90
half = 180
neghalf = -180
xcord = -280
ycord = -120

def draw_court():
    ball = turtle.Turtle()
    ball.shape("turtle")
    ball.color("white")
    ball.penup()
    ball.goto(xcord, ycord)
    ball.pendown()
    draw_floor(ball)
    draw_halfcourt(ball)
    draw_logo(ball)
    draw_leftthreepointline(ball)
    draw_rightthreepointline(ball)
    draw_foulleft(ball)
    draw_semicircle1(ball)
    draw_foulright(ball)
    draw_semicircle2(ball)
    draw_basketball(ball)

size = 6
width = 94 * size
height = 50 * size
r_middle = 6 * size
r_large = 22 * size
rect_height = 12 * size
rect_width = 12 * size

def draw_floor(ball):
    ball.forward(width)
    ball.left(right)
    ball.forward(height)
    ball.left(right)
    ball.forward(width)
    ball.left(right)
    ball.forward(height)

def draw_halfcourt(ball):
    ball.penup()
    ball.left(right)
    ball.forward(width/2)
    ball.left(right)
    ball.pendown()
    ball.forward(height)

def draw_logo(ball):
    ball.penup()
    ball.left(half)
    ball.forward(height/2)
    ball.right(right)
    ball.forward(r_middle)
    ball.left(right)
    ball.pendown()
    ball.circle(r_middle)

def draw_leftthreepointline(ball):
    ball.penup()
    ball.right(right)
    ball.forward(width/2 - r_middle)
    ball.left(right)
    ball.forward(r_large)
    ball.left(right)
    ball.pendown()
    ball.circle(r_large,half)

def draw_rightthreepointline(ball):
    ball.penup()
    ball.left(half)
    ball.forward(width)
    ball.left(half)
    ball.pendown()
    ball.circle(r_large,half)

def draw_foulleft(ball):
    ball.penup()
    ball.left(right)
    ball.forward(r_large - rect_height/2)
    ball.pendown()
    ball.left(right)
    ball.forward(rect_width)
    ball.right(right)
    ball.forward(rect_height)
    ball.right(right)
    ball.forward(rect_width)

def draw_semicircle1(ball):
    ball.penup()
    ball.left(half)
    ball.forward(rect_width)
    ball.pendown()
    ball.circle(r_middle, half)

def draw_foulright(ball):
    ball.penup()
    ball.left(half)
    ball.forward(width - rect_width)
    ball.left(half)
    ball.pendown()
    ball.forward(rect_width)
    ball.left(right)
    ball.forward(rect_height)
    ball.left(right)
    ball.forward(rect_width)

def draw_semicircle2(ball):
    ball.penup()
    ball.left(half)
    ball.forward(rect_width)
    ball.right(half)
    ball.pendown()
    ball.circle(r_middle, neghalf)

def draw_basketball(ball):    
    ball.penup()
    ball.forward(210)
    ball.left(90)
    ball.forward(10)
    ball.pendown()
    ball.fillcolor("brown")
    ball.begin_fill()
    radius = 30
    ball.circle(radius)
    ball.end_fill()
    ball.color("white")
    ball.left(90)
    ball.forward(60)
    ball.penup()
    for _ in range(2):
        ball.right(90)
        ball.forward(30)
    ball.pendown()
    ball.right(90)
    ball.forward(60)
    
def main():
    window = turtle.Screen()
    window.bgcolor("palegoldenrod")
    draw_court()
    window.exitonclick()

main()
