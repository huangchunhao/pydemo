# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 0021 21:19
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : classtest.py
# @Software: PyCharm
from demo_class.user import User

##测试给类变量，使用实例赋值和使用类赋值的区别

# 使用类赋值
print("没有赋值之前：", User.__dir__(User()))
print("没有赋值之前，User.name：", User.name)
print("没有赋值之前，User.age：", User.age)
# 使用类赋值
User.name = "类赋值"
User.age = "10000"
User.new = "new"  # 这里是没有任何作用的
print("使用类赋值之后：", User.__dir__(User()))
print("使用类赋值之后，User.name：", User.name)
print("使用类赋值之后，User.age：", User.age)
# 使用实例赋值
user = User()
user.name = "实例赋值"
user.new = "new"
# print("使用实例赋值之后：",User.__dir__(user))
print("使用实例赋值之后：", user.__dir__())
print("使用实例赋值之后，User.name：", User.name)
print("使用实例赋值之后，user.age：", user.age)
print("使用实例赋值之后，user.name：", user.name)
