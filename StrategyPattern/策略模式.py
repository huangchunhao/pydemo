# -*- coding: utf-8 -*-
# @Time    : 2019/11/23 0023 11:05
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : 策略模式.py
# @Software: PyCharm

#https://www.cnblogs.com/ydf0509/p/8527515.html

class People(object):
    def sayJob(self):
        pass


class Student(People):
    def __init__(self):
        pass

    def sayJob(self):
        print("I am a {}".format("student"))

class Teacher(People):
    def __init__(self):
        pass

    def sayJob(self):
        print("I am a {}".format("teacher"))


#具体策略类
class Factory(object):
    def __init__(self,people):
        self.people=people

    def sayJob(self):
        self.people.sayJob()



f1=Factory(Student())
f2=Factory(Teacher())

f1.sayJob()
f2.sayJob()