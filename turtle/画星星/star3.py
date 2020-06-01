from turtle import *
from random import *

clr = ['yellow', 'pink', 'cyan', 'white']

speed(10)
bgcolor("black")
width(6)
for i in range(50):
    penup()
    goto(randint(-400, 400), randint(-300, 300))
    pendown()
    color(clr[randint(0,3)])
    for j in range(5):
        forward(16)
        right(144)

done()