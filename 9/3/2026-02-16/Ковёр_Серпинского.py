from turtle import *
speed(1000)
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
        forward(y)
    if(i == "L"):
        left(120)
    if(i == "R"):
        right(120)
done()