import pygame

window = pygame.display.set_mode((800,794))
red = (200,0,0)

circleX = 400
circleY = 397
radius = 397

active = True

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False

   pygame.draw.circle(window,red,(circleX,circleY),radius) 

   pygame.display.update()

   pygame.display.get_window_size()
