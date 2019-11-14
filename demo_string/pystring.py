# -*- coding: utf-8 -*-
# @Time    : 2019/9/28 0028 16:36
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : pystring.py
# @Software: PyCharm
import time
#python3 直接支持Unicode

print(ord('A'))#65
print(ord('高'))#39640
print(chr(66))#B

#单双引号  和 三个引号
a= "I'm a teacher"
b= 'my name is “Tom”'
c='''
name="hhh"
compay="sxt"  age=18
lover="tom"
'''

print(a)
print(b)
print(c)

#空字符串  和 字符长度
d=''
print(len(d))#0
print(len("好"))#1
print(len("hhh"))#3


print("##"*5)

#不换行
print("aa",end='')
print("bb",end='\n')
print("cc",end='\t')
print("dd")
#aabb
#cc	dd


#从控制台获取字符串
#print(input("请输入内容"))


#str()  实现数字转型字符串
print(str(5.20))
print(str(3.14e2))
print(str(True))
# 5.2
# 314.0
# True

#使用[]提取字符
#正向搜索：
#最左侧第一个字符，偏移量是0，第二个是1，直到len(str)-1
#反向搜索：
#最右侧第一个字符，偏移量是-1，倒数第二个偏移量是-2，直到-len(str)
str1='0123456789abcdef'
print(str1[0])#0
print(str1[1])#1
print(str1[len(str1)-1])#f
print(str1[-1])#f
print(str1[-2])#e
print(str1[-len(str1)])#0


#replace  会创建新的字符串
strnew=str1.replace('f','ff')
print(str1)#0123456789abcdef
print(strnew)#0123456789abcdeff

#字符串切片slice操作,,包头不包尾
str1='0123456789abcdef'
slicestr=str1[:]
print(slicestr)#0123456789abcdef
print(str1[1:5])#1234
print(str1[1:5:2])#13 #2为步长
print(str1[2:])#23456789abcdef
print(str1[:5])#01234
print(str1[-8:-3])#89abc
print(str1[-3:])#def
print(str1[::-1])#fedcba9876543210  # 步进为1，反向提取


#split()   jion()

#split()分割  基于指定分隔符将字符串分割成多个字符串，并保存在列表中，如果不指定分割符，则默认使用空白字符（换行符、空格、制表符）
sp="to be or not to be"
print(sp.split())#['to', 'be', 'or', 'not', 'to', 'be']
print(sp.split('be'))#['to ', ' or not to ', '']
#jion()  将一系列字符串连接起来
ji=['sxt','sxt100','sxt200']
print(''.join(ji))#sxtsxt100sxt200
print('##'.join(ji))#sxt##sxt100##sxt200

#拼接字符串要点
#使用字符串拼接符+，会生成新的字符串对象，因此不推荐使用+来拼接字符串。推荐使用join函数，因为join函数在拼接字符串之前会计算所有字符串的长度，然后逐一拷贝，仅新疆一次对象。



time01= time.time()
add=''
for _ in range(10000000):
    a+="sxt"
time02= time.time()

print("add运算时间："+str(time02-time01))#1000000=>add运算时间：0.5854620933532715 #10000000=>add运算时间：45.11636757850647


time03= time.time()
li=[]
for _ in range(10000000):
    li.append("sxt")
''.join(li)
time04= time.time()
print("jion运算时间："+str(time04-time03))#1000000=>jion运算时间：0.09975719451904297 #10000000=>jion运算时间：1.0601732730865479




