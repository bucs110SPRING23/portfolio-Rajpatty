import random

x = random.randint(1,1000)

correct = x
tries = float('inf')

attempts = 0

while tries != 0:
  attempts += 1
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
  
print(attempts)