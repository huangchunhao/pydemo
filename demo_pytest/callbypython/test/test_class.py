# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 0013 20:44
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : test_class.py
# @Software: PyCharm

class TestClass(object):


    def test_one(self):
        x = "this"
        assert 'h' in x

    def test_two(self):
        x = "hello"
        assert x=='hello'