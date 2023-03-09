import turtle 
import random

window = turtle.Screen() 
window.bgcolor('lightblue')

michelangelo = turtle.Turtle() 
leonardo = turtle.Turtle()
michelangelo.color('orange')
leonardo.color('blue')
michelangelo.shape('turtle')
leonardo.shape('turtle')

michelangelo.up() 
leonardo.up()
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

leonardo.forward(100)
michelangelo.forward(100)
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)

for i in range(10):
    michelangelo.forward(random.randrange(1,10))
    leonardo.forward(random.randrange(1,10))
michelangelo.goto(-100,20)
leonardo.goto(-100,-20)
window.exitonclick()

import pygame
import math

pygame.init()

window = pygame.display.set_mode()
points = []
num_side = [3,4,6,20,100,360]
color = ["brown", "cadetblue", "cyan", "gold", "darkolivegreen", "darkred"]
side_length = 150

xpos = 725
ypos = 400

for s in range(len(num_side)):
    for i in range(num_side[s]):
        angle = 360/num_side[s]
        radians = math.radians(angle*i)
        x = xpos + side_length*math.cos(radians)
        y = ypos + side_length*math.sin(radians)
        points.append([x,y])
    pygame.draw.polygon(window, color[s], points)
    pygame.display.flip()
    pygame.time.wait(1000)
    window.fill("burlywood")
    pygame.display.flip()
    points = []
    
window.exitonclick()
