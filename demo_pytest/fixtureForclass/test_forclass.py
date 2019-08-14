# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 15:05
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : test_forclass.py
# @Software: PyCharm
import pytest


@pytest.mark.usefixtures("declass","declass2")
class TestClass(object):
    def test_case1(self):
        print("test_case1:")
        assert 0==0


    def test_case2(self):
        print("test_case2:")
        assert 0 == 0