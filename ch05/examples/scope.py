"""
def bar(x=0, y=2, z=3):
    print(x,y,z)

bar(z=1,x=2)
bar()

def foo():
    local_var = 5 
    x = 2

def foo():
    local_var = 5
    print(x)

global_var = 5

f(x) = y

def foo():
    x = 5 
    return x

y = foo()
print(y) 

def foo():
    x = 5 
    if x > 5:
        return x
    else:
        return 5

y = foo()
print(y) 

def my_func(x=0):
    return x + x #scoped to my_func

my_func(5)
print(x)


def powerof(x=0, p=0):
    power = p 
    y = x ** power
    return y

power = 2
result = powerof(5,3)
print(result)

def foo():
    x = 5
    print(x*x)
    return(x*x)

def foo2():
    x = 5
    return(x*x)

print(foo())
print(foo2())

import random
print(foo(abs(-42)), ord("2"))
print("3",foo2())

print("4",foo(random.randint(1,10)))
"""
var = 5

def start(var):
    return True

def dosomething():
    print(5)

def main():
    x = 5
    start(x)
    start(x)
    dosomething()

main()



