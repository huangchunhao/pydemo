# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 12:22
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : four.py
# @Software: PyCharm

import turtle


turtle.setup(600,400,0,0)
turtle.bgcolor("red")
turtle.fillcolor("yellow")
turtle.color('yellow')
turtle.speed(10)
#主星
turtle.begin_fill()
turtle.up()
turtle.goto(-280,100)
turtle.down()
for i in range (5):
    turtle.forward(150)
    turtle.right(144)
turtle.end_fill()

#第1颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-100,180)
turtle.setheading(305)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.left(144)

turtle.end_fill()


#第2颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-50,110)
turtle.setheading(30)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.right(144)

turtle.end_fill()

#第3颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-40,50)
turtle.setheading(5)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.right(144)

turtle.end_fill()

#第4颗副星
turtle.begin_fill()
turtle.up()
turtle.goto(-100,10)
turtle.setheading(300)
turtle.down()
for i in range (5):
    turtle.forward(50)
    turtle.left(144)

turtle.end_fill()

turtle.done()