# -*- coding: utf-8 -*-
# @Time    : 2019/11/24 0024 12:01
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : 适配器模式.py
# @Software: PyCharm




class Student(object):
    def sayJob(self):
        print("I am a {}".format("student"))

class Monitor(object):
    def sayMonitor(self):
        print("I am a {}".format("monitor"))

class Adapter(Student):
    def __init__(self):
        self.Monitor=Monitor()

    def trans(self):
        self.Monitor.sayMonitor()


if __name__ == "__main__":
    target = Adapter()
    target.trans()