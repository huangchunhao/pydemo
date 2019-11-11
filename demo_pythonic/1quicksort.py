# -*- coding: utf-8 -*-
# @Time    : 2019/11/11 0011 20:40
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : 1quicksort.py
# @Software: PyCharm

def quicksort(array):
    print("*"*20)
    print("原始：")
    print(array)
    less=[];greater=[]
    if len(array)<=1:
        print("结果1：")
        print(array)
        return array
    pivot=array.pop()
    print(pivot)
    for x in array:
        if x<= pivot:
            less.append(x)
            # print("less:")
            # print(less)
        else:
            greater.append(x)
            # print("greater:")
            # print(greater)
    result=quicksort(less)+[pivot]+quicksort(greater)
    print("结果2：")
    print(result)
    return result

quicksort([9,8,4,5,32,64,2,1,0,10,19,27])

#quicksort([9,8,4,5])
