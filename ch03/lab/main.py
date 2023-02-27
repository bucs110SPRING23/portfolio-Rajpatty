import pygame
pygame.init()

window = pygame.display.set_mode((800,794))
green = (0,139,69,255)
red = (205,51,51,255)
blue = (0,0,255,255)

circleX = 400
circleY = 397
radius = 397

active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False
   pygame.display.flip()

   pygame.draw.circle(window,green,(circleX,circleY),radius) 
   pygame.draw.line(window,red,(398,0),(398,794),width=3)
   pygame.draw.line(window,red,(796,397),(3,397),width=3)

import random
import math

pygame.init()

SCREEN = window

LENGTH = 5
WIDTH = 5
RADIUS = 5

LOOPCOUNT = 10
MINPOS = 0
MAXPOS = 796
MAXPOS2 = 794

SOLID = 0
for i in range(LOOPCOUNT):
    LEFT = random.randint(MINPOS,MAXPOS)
    TOP = random.randint(MINPOS,MAXPOS)

COLOR = (0,0,255,255)

CIRCLEPOS = (random.randint(MINPOS,MAXPOS), random.randint(MINPOS,MAXPOS2)) 
pygame.draw.circle(SCREEN, COLOR, CIRCLEPOS, RADIUS, SOLID)

pygame.display.update()

while True:
    for events in pygame.event.get():
        if events.type == pygame.QUIT:
            pygame.quit()