# -*- coding: utf-8 -*-
# @Time    : 2019/11/24 0024 10:41
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : 建造者模式.py
# @Software: PyCharm

from abc import ABCMeta, abstractmethod

class Builder():
    __metaclass__ = ABCMeta

    @abstractmethod
    def sayName(self):
        pass

    @abstractmethod
    def sayAge(self):
        pass

    @abstractmethod
    def sayJob(self):
        pass

class Student(Builder):

    def sayName(self):
        print("My name is {}".format("Tom"))


    def sayAge(self):
        print("I am {} years old".format("Ten"))


    def sayJob(self):
        print("I am a {}".format("Student"))


class Teacher(Builder):

    def sayName(self):
        print("My name is {}".format("Helen"))

    def sayAge(self):
        print("I am {} years old".format("twenty"))

    def sayJob(self):
        print("I am a {}".format("Teacher"))


class Director():
    def __init__(self, Builder):
        self.Builder = Builder

    def say(self): #功能组合   这个和策略模式有区别，策略模式功能都是单独的
        self.Builder.sayName()
        self.Builder.sayAge()
        self.Builder.sayJob()

if __name__=='__main__':
    director_Student = Director(Student())
    director_Teacher = Director(Teacher())
    director_Student.say()
    director_Teacher.say()