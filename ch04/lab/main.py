import pygame
import random
import math
pygame.init()

screenwidth = 800
screenheight = 794
screensize = [screenwidth,screenheight]
window = pygame.display.set_mode((screensize))

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
   

SCREEN = window

score = 0

LENGTH = 5
WIDTH = 5
RADIUS = 5

LOOP = 10
MINPOS = 0
MAXPOS = 796

SOLID = 0

COLOR = (102,205,170,255)
COLOR2 = (220,20,60,255)
COLOR3 = (250,128,114,255)
COLOR4 = (78,238,149,255)

LEFT = random.randrange(MINPOS,MAXPOS)
TOP = random.randrange(MINPOS,MAXPOS)
distance_from_center = math.hypot(LEFT-398,TOP-398)
is_in_circle = distance_from_center <= screenwidth/2
        
for i in range(LOOP):
    
    if is_in_circle:
        pygame.draw.circle(SCREEN, COLOR, [LEFT,TOP], RADIUS, SOLID)
    else:
        pygame.draw.circle(SCREEN, COLOR2, [LEFT,TOP], RADIUS, SOLID)

for i in range(LOOP):
    
    if is_in_circle:
        pygame.draw.circle(SCREEN, COLOR3, [LEFT,TOP], RADIUS, SOLID)
    else:
        pygame.draw.circle(SCREEN, COLOR4, [LEFT,TOP], RADIUS, SOLID)



pygame.display.update()

running = True

while running:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()