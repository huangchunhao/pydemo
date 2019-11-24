# -*- coding: utf-8 -*-
# @Time    : 2019/11/24 0024 13:12
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : 修饰器模式.py
# @Software: PyCharm


def sayName(func):
    def _sayName():
        print("begin")
        func()
        print(func.__name__)
        print("over")
    return _sayName

@sayName
def student():
    print("I am a {}".format("student"))
    return "ok"


student()
print(student)#<function sayName.<locals>._sayName at 0x000001C6F5277948>
print("help:")
help(student)#Help on function _sayName in module __main__:

            #_sayName()

print("##"*30)



import functools
def sayName2(func):
    @functools.wraps(func) #这里使用了functools.wraps，保证了student2函数属性不丢失#https://www.cnblogs.com/fcyworld/p/6239951.html
    def _sayName2():
        print("begin")
        func()
        print(func.__name__)
        print("over")
    return _sayName2

@sayName2
def student2():
    print("I am a {}".format("student"))
    return "ok"

student2()
print(student2) #<function student2 at 0x000001C6F52799D8>
print("help:")
help(student2)  #Help on function student2 in module __main__:

                #student2()