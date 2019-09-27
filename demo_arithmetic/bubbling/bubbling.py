# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 8:53
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : bubbling.py
# @Software: PyCharm

data=[9,5,3,2,4,5,6,1,0,7,8,6]

wi=len(data)-1
num=0
for i in range(wi):
    for j in range(wi-i):
        num+=1
        if data[j] > data[j+1]:
            data[j] ,data[j + 1]=data[j + 1],data[j]


print(data)
print(num)