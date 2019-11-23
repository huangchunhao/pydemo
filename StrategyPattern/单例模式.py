# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 0023 11:39
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : 单例模式.py
# @Software: PyCharm

class Singleton(object):
    def __init__(self):
          pass

    def __new__(cls, *args, **kwargs):
        if not hasattr(Singleton, "_instance"): # 反射
            Singleton._instance = object.__new__(cls)
        return Singleton._instance

obj1 = Singleton()
obj2 = Singleton()
print(obj1, obj2)