# -*- coding: utf-8 -*-
# @Time    : 2019/11/24 0024 9:12
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : else用法.py
# @Software: PyCharm

def else1(num):
    for i in range(num):
        if(i>10):
            break
        print(i)
    else:
        print("over")


# else1(5)
# print("##"*20)
# else1(20)


def else2(num):
    while num > 0:
        if(num==10):
            break
        num-=1
        print(num)
    else:
        print("over")


# else2(5)
# print("##"*20)
# else2(20)

def ex(num):
    if(num==10):
        raise BaseException("BaseException!")

def else3(num):
    try:
        for i in range(num):
            ex(i)
            print(i)
    except BaseException as msg:
        print(msg)
    else:
        print("over")
    finally:
        print("end")

else3(5)
print("##"*20)
else3(20)