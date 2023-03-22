def multiply(x=0,y=0):
    theta = 0
    for i in range(y):
        theta = theta + x
    return theta

def powerof(x=0, p=0):
    power = p 
    y = x ** power
    return y

def poweroftwo(x=0):
    return multiply(x,x)
    

def main():
    x = int(input("enter number:"))
    y = int(input("enter number:"))
    p = int(input("enter number:"))
    number = powerof(x,p)
    print(number)
    number = multiply(x,y)
    print(number)
    number = poweroftwo(x)
    print(number)

main()
    
    