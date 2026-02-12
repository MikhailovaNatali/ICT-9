from turtle import *
def a(n, k):
    b = 10
    left(90)
    for i in range(n):
        right(115)
        forward(b)
        backward(b)
        right(130)
        forward(b)
        backward(b)
        left(65)
        forward(k)
        right(180)
        b = b + 10
a(7, 10)
done()