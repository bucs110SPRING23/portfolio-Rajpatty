import turtle

class Num:

    def __init__(self,n)->None:
        self.data = n
        self.x = "string"

class Foo:
    def __init__(self,**kwargs->None):
        print(kwargs)

def main()->None:
    mynum = Num(7)
    mynum2 = Num(9)
    mynum3 = {'data':7,"x":"string"}

    print(mynum.data)
    print(mynum2.data)
    print(mynum3['data'])
    print(mynum.__dict__)

    dictionary = {'x':1, 'y':2, 'z':3}


    "t = turtle.Turtle()"
    "t.forward(56)"

    "mylist = []"



main()