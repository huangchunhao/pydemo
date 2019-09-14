# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 0021 21:16
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : user.py
# @Software: PyCharm
class User():
    name="hello"
    age="18"

    def info(self):
        print("name:",self.name)
        print("age:", self.age)

print("--*"*20)

def printv(i,j):
    i=6
    print("i的内存地址",id(i))#i的内存地址 140725476422048
    print("i的值",i)#i的值 6
    print("j的内存地址",id(j))#j的内存地址 2908009218864
    print("j的值",j)#j的值 5000

n=5
m=5000
print("n的内存地址",id(n))#n的内存地址 140725476422016
print("m的内存地址",id(m))#m的内存地址 2908009218864
print("n的值",n)#n的值 5
print("m的值",m)#m的值 5000
printv(n,m)
print("n的值",n)#n的值 5
print("m的值",m)#m的值 5000

print("--*"*20)

def printid(user):
    user.age=20
    print("函数中user内存地址：",id(user))#函数中user内存地址： 2254536402504
    print("函数中user内容：",user.__dict__)#函数中user内容： {'age': 20}

u=User()
u.age=30
print("u对象内容：",u.__dict__)#u对象内容： {'age': 30}
print("u内存地址：",id(u))#u内存地址： 2254536402504
printid(u)
print("u对象内容：",u.__dict__)#u对象内容： {'age': 20}

print("--*"*20)