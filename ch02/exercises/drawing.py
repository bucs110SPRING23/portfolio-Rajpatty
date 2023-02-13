import turtle 
gamma = turtle.Screen()
beta = turtle.Turtle()

beta.color("blue")

sides = int(input("How many sides?"))

for i in range(sides):
    length = int(input("How long is each side?"))

    beta.forward(length)
    beta.right(360 / sides)

turtle.done()