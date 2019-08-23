# -*- coding: utf-8 -*-
# @Time    : 2019/8/23 9:24
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : functest.py
# @Software: PyCharm

def func():
    def _func():
        print("func")
    return _func


def funcp():
    def _funcp(param):
        print(param)
    return _funcp

func()()

funcp()("5555")