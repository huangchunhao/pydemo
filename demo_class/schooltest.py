# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 0021 21:46
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : schooltest.py
# @Software: PyCharm
from demo_class.school import School

school=School("test","test_add")
print(school.__dict__)
print(school.__dir__())
school.info="东大","南京"
print(school.__dict__)
print(school.__dir__())
print(school.common)
print(school.__dict__)
print(school.__dir__())
print(school.common)

