import random
from turtle import *
tracer(0)
x = 12
y = 2
st = "FX"
for a in range(x):
    i = 0
    while i < len(st):
        if(st[i] == "X"):
            st = st[:i] + "XRYFR" + st[i+1:]
            print(st)
            i = i + 5
        if(i < len(st)):
            if (st[i] == "Y"):
                st = st[:i] + "LFXLY" + st[i+1:]
                i = i + 5
            else:
                i = i + 1
        
        
print(st)
for i in st:
    if(i == "F"):
        a = random.randint(1, 3)
        if a == 1: 
            color("dark blue")
        if a == 2: 
            color("light sky blue")
        if a == 3: 
            color("steel blue")
        forward(y)
    if(i == "L"):
        left(90)
    if(i == "R"):
        right(90)
done()