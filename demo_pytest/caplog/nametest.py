# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 18:04
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : nametest.py
# @Software: PyCharm

from pydemo.demo_pytest.caplog.caplogtest import *
import re

t=TestClass()

dirs=t.__dir__()
print(dirs)
c=re.compile(r'test_')
content=[]
for dir in dirs:
    p=c.findall(dir)
    if(p.__len__()>0):
        content.append(dir)

print(content)

