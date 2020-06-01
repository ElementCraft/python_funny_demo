# 带有颜色渐变的大星星

import turtle 

for i in range(50):
    turtle.pencolor(i / 50, i / 50, i / 50)
    turtle.forward(i * 12)
    turtle.right(144)
    
turtle.done()