# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 14:27
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : two.py
# @Software: PyCharm

import threading


class FKThread(threading.Thread):
    def __init__(self):
        threading.Thread.__init__(self)
        self.i=0

    def run(self):
        while self.i<100:
            print(threading.current_thread().getName() + "  --- " + str(self.i))
            self.i +=1


for i in range(100):
    print(threading.current_thread().getName() + "  --- " + str(i))
    if i==20:
        t1=FKThread()
        t1.setName("AAAA")
        t1.start()
        t2 = FKThread()
        t2.setName("BBBB")
        t2.start()
print("主线程完成")