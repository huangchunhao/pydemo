# -*- coding: utf-8 -*-
# @Time    : 2019/12/11 10:08
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : timetest.py
# @Software: PyCharm
import time,datetime,string

print(time.localtime(time.time()))
print(type(time.localtime(time.time())))
print(time.strftime("%Y%m%d%H%M%S",time.localtime(time.time())))



print(datetime.datetime.now())
print(type(datetime.datetime.now()))