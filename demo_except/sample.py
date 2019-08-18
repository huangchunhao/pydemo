# -*- coding: utf-8 -*-
# @Time    : 2019/8/18 0018 17:47
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : sample.py
# @Software: PyCharm

def ex():
    raise Exception("excepting")

if __name__ == "__main__":
    try:
        print("123")
        ex()
        print("456")
    except Exception as e:
        print("789")
        print(type(e))
        print(e.__str__())
    else:
        print('没有出现异常')#没有异常时才会执行
    finally:
        print('资源回收')



