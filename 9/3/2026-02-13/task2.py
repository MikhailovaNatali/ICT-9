from turtle import *
def f(x):
    return 2*x + 69

for i in range(4):
    forward(300)
    backward(300)
    right(90)

for i in range(200):
    teleport(i, f(i))
    forward(0.5)
left(180)
for i in range(200):
    teleport(-i, f(-i))
    forward(1)
done()