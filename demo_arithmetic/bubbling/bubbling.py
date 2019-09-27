# -*- coding: utf-8 -*-
# @Time    : 2019/9/27 8:53
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : bubbling.py
# @Software: PyCharm

data=[9,5,3,2,4,5,6,8,9,7,8,9]
data2=[9,5,3,2,4,5,6,8,9,7,8,9]

def common_bubble_sort(data):
    wi = len(data) - 1
    num = 0
    for i in range(wi):
        for j in range(wi - i):
            num += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
    print(data)
    print(num)

def flag_bubble_sort(data):
    wi = len(data) - 1
    num = 0
    for i in range(wi):
        flag = False
        for j in range(wi - i):
            num += 1
            if data[j] > data[j + 1]:
                data[j], data[j + 1] = data[j + 1], data[j]
                flag=True
        if not flag:
            print(data)
            print(num)
            return




print("common_bubble_sort")
common_bubble_sort(data)
print("flag_bubble_sort")
flag_bubble_sort(data2)
