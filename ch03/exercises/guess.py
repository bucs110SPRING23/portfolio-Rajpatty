import random

x = random.randint(1,10)

correct = x
tries = 3

while tries != 0:
  guess = int(input())
  if guess > x :
    print("too high")
    tries -= 1
  elif guess < x:
    print("too low")   
    tries -= 1
  elif guess == x:
    print("correct!")
    break
    
if tries == 0:
  print("get better ¯\_(ツ)_/¯")

  