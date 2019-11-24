# -*- coding: utf-8 -*-
# @Time    : 2019/11/24 0024 10:25
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : 工厂模式.py
# @Software: PyCharm

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
    def __init__(self,jobmode):
        self.jobmode=jobmode

    def getPeople(self):
        if(self.jobmode==1):
            return Student()
        elif(self.jobmode==2):
            return Teacher()



f1=Factory(1).getPeople()
f2=Factory(2).getPeople()

f1.sayJob()
f2.sayJob()