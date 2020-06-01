from turtle import *
from random import *

bgcolor("black")
width(6)
color("yellow")

for i in range(50):
    penup()
    goto(randint(-400, 400), randint(-300, 300))
    pendown()
    for j in range(5):
        forward(16)
        right(144)

done()