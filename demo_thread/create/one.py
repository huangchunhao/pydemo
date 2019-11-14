# -*- coding: utf-8 -*-
# @Time    : 2019/11/7 14:02
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : one.py
# @Software: PyCharm

import threading

def action(max):
    for i in range(max):
        print(threading.current_thread().getName()+"  --- "+str(i))


for i in range(100):
    print(threading.current_thread().getName() + "  --- " + str(i))
    if i==20:
        t1=threading.Thread(target=action,args=(100,))
        t1.setName("AAAA")
        t1.start()
        t2 = threading.Thread(target=action, args=(100,))
        t2.setName("BBBB")
        t2.start()
print("主线程完成")