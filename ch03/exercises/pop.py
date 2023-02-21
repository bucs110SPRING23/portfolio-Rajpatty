import pygame 
import math

pygame.init()
window = pygame.display.set_mode()

aqua = (0,255,255,255)
azure = (240,255,255,255)

points = list(input())
num_sides = int(input())
side_length = int(input())
xpos = int(input())
ypos = int(input())
angle = 360/num_sides
radians = math.radians(angle * (3.14 // 180))
x = xpos + side_length * math.cos(radians)
y = ypos + side_length * math.sin(radians)

X = 400
Y = 400

display_surface = pygame.display.set_mode((X,Y))

display_surface.fill(aqua)

for i in range(6):
    pygame.draw.polygon(window, azure, [(0,0),(200,0),(0,200),(200,200)],x,y)

    
window.exitonclick()