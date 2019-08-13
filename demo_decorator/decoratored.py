# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 0013 20:08
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : decoratored.py
# @Software: PyCharm

from demo_decorator.decoratortest import *

@de1
def use1():#被装饰的函数不带形参
    print("use1")


@de2
def use2(name, age, sex="male", height=170):  # 被装饰的函数带形参
    print(name, age, sex, height)


@de3("use3","de3",url="http://www.baidu.com")
def use3():
    print("use3")

@de4
@de5
def use5():
    print("use5")