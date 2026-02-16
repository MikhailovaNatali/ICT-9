from turtle import *
tracer(0)
#teleport(-250, 130)
x = 12
y = 2
st = "FX"
for a in range(x):
    i = 0
    print("asdfghjkl")
    while i < len(st):
        if(st[i] == "X"):
            st = st[:i] + "XRYFR" + st[i+1:]
            print(st)
            i = i + 5
        if(i < len(st)):
            print("ertyuio")
            if (st[i] == "Y"):
                print("zxcvbnm")
                st = st[:i] + "LFXLY" + st[i+1:]
                i = i + 5
            else:
                print("qwerfghyujkl")
                i = i + 1
        
        
print(st)
for i in st:
    if(i == "F"):
        forward(y)
    if(i == "L"):
        left(90)
    if(i == "R"):
        right(90)
done()