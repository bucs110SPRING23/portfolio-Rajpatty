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

window.exitonclick()
