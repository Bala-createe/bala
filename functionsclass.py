a=1
#calculate area of the square
def sqrarea(a=0):
    if a==0:
        print("value is not passed")
        return "value is not passed"
    else:
        print(a*a)
        return (a*a),"sqr"
def sqlofrect(w,b):
    print(w*b)

def mysum(*values):
    output=0
    print(type(values))
    for i in values:
        output+=int(i)
    return output

def keyarbargs(**values):
    print(type(values))
    print(values['a'])

print(keyarbargs(a=1,b=2,c=3))
print(mysum(1,2,3,10,20,30,40,20))
print(sqlofrect(b=10,w=4))
print()

import random
"""
a=sqrarea(10)
print(a)
sqrarea(100)
sqrarea(200)
sqrarea(300)
b=sqrarea()
print(b)
sqlofrect(10,10)"""