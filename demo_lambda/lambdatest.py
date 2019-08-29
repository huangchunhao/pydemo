# -*- coding: utf-8 -*-
# @Time    : 2019/8/16 13:54
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : lambdatest.py
# @Software: PyCharm
import uuid

a=lambda :str(uuid.uuid4())
print(a())


b=lambda x:str(uuid.uuid4())+str(x)
print(b("xxxxxxx"))

c=lambda :(str(uuid.uuid4()),str(uuid.uuid4()))
c1,c2=c()
print(c1)
print(c2)


d=lambda x=str(uuid.uuid4()):(x,x+"xxxxxxx")
print(d())