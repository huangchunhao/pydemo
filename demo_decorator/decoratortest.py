# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 0013 20:07
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : decoratortest.py
# @Software: PyCharm


def de1(func):
    def content():
        print("begin1")
        func()
        print("end1")
    return content


def de2(func):
    def content(*args,**kwargs):
        print("begin2")
        print(args,kwargs["sex"])
        print("end2")
    return content



def de3(*args,**kwargs):  #装饰器函数带形参
    def first(func):
        def content():
            print("begin3")
            print(args, kwargs)
            print("end3")
        return content
    return first



def de4(func):
    def content():
        print("begin4")
        func()
        print("end4")
    return content


def de5(func):
    def content():
        print("begin5")
        func()
        print("end5")
    return content