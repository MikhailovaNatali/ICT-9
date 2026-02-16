import random
from turtle import *
speed(10000)
teleport(-200, -50)
x = 5
y = 10
st = "FLGLG"
for a in range(x):
    i = 0
    while i < len(st):
        if(st[i] == "F"):
            st = st[:i] + "FLGRFRGLF" + st[i+1:]
            i = i + 8
        if(i < len(st)):
            if (st[i] == "G"):
                st = st[:i] + "GG" + st[i+1:]
                i = i + 2
            else:
                i = i + 1
print(st)
for i in st:
    if(i == "F" or i == "G"):
        a = random.randint(1, 5)
        if a == 1: 
            color("dark blue")
        if a == 2: 
            color("light sky blue")
        if a == 3: 
            color("steel blue")
        if a == 4: 
            color("midnight blue")
        if a == 5: 
            color("royal blue")
        forward(y)
    if(i == "L"):
        left(120)
    if(i == "R"):
        right(120)
done()