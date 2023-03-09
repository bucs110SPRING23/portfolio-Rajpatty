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

color = (255,0,0)
color2 = ("blue")

active = True


pygame.draw.rect(window, color, pygame.Rect(30, 30, 60, 60))
pygame.draw.rect(window, color2, pygame.Rect(700, 30, 60, 60))

while active:
   for event in pygame.event.get():
      if event.type == pygame.QUIT:
         active = False
   pygame.display.flip()
   for e in pygame.event.get():
        if e.type == pygame.QUIT:
            pygame.quit()
            exit()
        if e.type == pygame.MOUSEBUTTONDOWN:
            mx, my = pygame.mouse.get_pos()
            if mx < 400:
                pygame.display.flip()
                pygame.time.wait(1000)
                active = False
                print("you picked player 1")
                break 
            else:
                pygame.display.flip()
                pygame.time.wait(1000)
                active = False
                print("you picked player 2")
                break


   pygame.draw.circle(window,green,(circleX,circleY),radius) 
   pygame.draw.line(window,red,(398,0),(398,794),width=3)
   pygame.draw.line(window,red,(796,397),(3,397),width=3)
   

SCREEN = window

LENGTH = 5
WIDTH = 5
RADIUS = 5

LOOP = 20
MINPOS = 0
MAXPOS = 796

SOLID = 0

COLOR = (102,205,170,255)
COLOR2 = (220,20,60,255)
COLOR3 = (250,128,114,255)
COLOR4 = (78,238,149,255)

LEFT = random.randrange(MINPOS,MAXPOS)
TOP = random.randrange(MINPOS,MAXPOS)

beta = 2
theta = 0
alpha = [COLOR, COLOR3]
gamma = [COLOR2, COLOR4]
delta = [[],[]]
        
for i in range(LOOP):
    LEFT, TOP = random.randrange(MINPOS,MAXPOS), random.randrange(MINPOS,MAXPOS)
    distance_from_center = math.hypot(LEFT-398,TOP-398)
    is_in_circle = distance_from_center <= screenwidth/2

    if is_in_circle:
        pygame.draw.circle(SCREEN, alpha[theta], [LEFT,TOP], RADIUS, SOLID)
    else:
        pygame.draw.circle(SCREEN, gamma[theta], [LEFT,TOP], RADIUS, SOLID)
    
    delta[theta].append(is_in_circle)

    theta = (theta + 1) % beta

    pygame.display.flip()
    
    pygame.time.wait(500)

for i in range(beta):
    if sum(delta[0]) > sum(delta[1]):
        font = pygame.font.Font(None, 48)
        text = font.render("Player 1 wins", True, "white")
        SCREEN.blit(text, (0, 0))
    elif sum(delta[0]) < sum(delta[1]):
        font = pygame.font.Font(None, 48)
        text = font.render("Player 2 wins", True, "white")
        SCREEN.blit(text, (0, 0))
    else:
        font = pygame.font.Font(None, 48)
        text = font.render("tie", True, "white")
        SCREEN.blit(text, (0, 0))
pygame.display.flip()

if mx < 400:
    if sum(delta[0]) > sum(delta[1]):
        font = pygame.font.Font(None, 48)
        text = font.render("You are correct", True, "white")
        SCREEN.blit(text, (0, 100))
    elif sum(delta[0]) < sum(delta[1]):
        font = pygame.font.Font(None, 48)
        text = font.render("You are wrong", True, "white")
        SCREEN.blit(text, (0, 100))
if mx > 400:
    if sum(delta[0]) > sum(delta[1]):
        font = pygame.font.Font(None, 48)
        text = font.render("You are wrong", True, "white")
        SCREEN.blit(text, (0, 100))
    elif sum(delta[0]) < sum(delta[1]):
        font = pygame.font.Font(None, 48)
        text = font.render("You are correct", True, "white")
        SCREEN.blit(text, (0, 100))
    else:
        font = pygame.font.Font(None, 48)
        text = font.render("It is a tie", True, "white")
        SCREEN.blit(text, (0, 100))

p = sum(delta[0])
s = sum(delta[1])

font = pygame.font.Font(None, 48)
text = font.render(f'Player 1 Score: {p}', True, "white")
SCREEN.blit(text, (0, 200))

font = pygame.font.Font(None, 48)
text = font.render(f'Player 2 Score: {s}', True, "white")
SCREEN.blit(text, (0, 300))

print((sum(delta[0])))
print((sum(delta[1])))

pygame.display.update()

pygame.time.wait(10000)

while active:
    for event in pygame.event.get():
        if event.type == pygame.QUIT:
            running = False
            exit()