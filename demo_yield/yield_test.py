# -*- coding: utf-8 -*-
# @Time    : 2019/8/20 0020 21:35
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : yield_test.py
# @Software: PyCharm
import uuid
import sys

def foo():
    print("starting...")
    while True:
        res = yield 4
        print("res----:",res)


g = foo()
print(next(g))
# starting...
# 4
print("*"*20)
# ********************
print(next(g))
# res----: None


#https://blog.csdn.net/mieleizhi0522/article/details/82142856
# 1.程序开始执行以后，因为foo函数中有yield关键字，所以foo函数并不会真的执行，而是先得到一个生成器g(相当于一个对象)
#
# 2.直到调用next方法，foo函数正式开始执行，先执行foo函数中的print方法，然后进入while循环
#
# 3.程序遇到yield关键字，然后把yield想想成return,return了一个4之后，程序停止，并没有执行赋值给res操作，此时next(g)语句执行完成，所以输出的前两行（第一个是while上面的print的结果,第二个是return出的结果）是执行print(next(g))的结果，
#
# 4.程序执行print("*"*20)，输出20个*
#
# 5.又开始执行下面的print(next(g)),这个时候和上面那个差不多，不过不同的是，这个时候是从刚才那个next程序停止的地方开始执行的，也就是要执行res的赋值操作，这时候要注意，这个时候赋值操作的右边是没有值的（因为刚才那个是return出去了，并没有给赋值操作的左边传参数），所以这个时候res赋值是None,所以接着下面的输出就是res:None,
#
# 6.程序会继续在while里执行，又一次碰到yield,这个时候同样return 出4，然后程序停止，print函数输出的4就是这次return出的4.




print("--"*20)
def intYield():
    for i in range(5):
        yield i

for i in intYield():
    print(i)

print("--"*20)
def funcYield():
    def _funcYield():
        for i in range(5):
            yield i
    return _funcYield


for i in funcYield()():
    print(i)

print("--"*20)
def func2Yield():
    def _func2Yield():
        for _ in range(5):
            yield uuid.uuid4()
    return _func2Yield


for i in func2Yield()():
    print(i)

print("--"*20)


#测试yield函数的执行顺序
def yield_test(n):
    for i in range(n):
        print(str(sys._getframe().f_lineno) + " before.")
        yield call(i)
        print(str(sys._getframe().f_lineno) + " after.")
        print('i====', i)  # 输出的是当前的i值
        print(str(sys._getframe().f_lineno) + " afterPrint.")


def call(i):
    return i * 2


#print(yield_test(4))  # <generator object yield_test at 0x0000000001DE9200>


for i in yield_test(3):
    print(str(sys._getframe().f_lineno) + " forb.")
    print('i=', i)  # 输出的是yield函数的返回值  yield函数，相当于一个return语句：下次迭代时候，代码从yield的下一个语句开始执行
    print(str(sys._getframe().f_lineno) + " fora.")



