# -*- coding: utf-8 -*-
# @Time    : 2019/9/14 0014 10:13
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : yield_turtle.py
# @Software: PyCharm

import turtle
t=turtle
t.width(10)

point=[(0,0,"blue"),(120,0,"black"),(240,0,"red"),(60,-50,"yellow"),(180,-50,"green")]
print(point)
def yield_turtle():
    for x, y,c in point:
        print(x,y)
        yield cricle(x,y,c)#  生成一个cricle集合

def cricle(x,y,c):
    t.color(c)
    t.penup()
    t.goto(x, y)
    t.pendown()
    t.circle(50)

for _ in yield_turtle():
    print("--")

# def cricle2(x,y):
#     t.penup()
#     t.goto(x, y)
#     t.pendown()
#     t.circle(50)
#
#
#
# for x,y in point:
#     cricle2(x,y)

