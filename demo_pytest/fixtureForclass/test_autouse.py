# -*- coding: utf-8 -*-
# @Time    : 2019/8/22 11:31
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : test_autouse.py
# @Software: PyCharm

import pytest


@pytest.mark.usefixtures("class_auto","funcion_for_method")
class TestClass(object):

    @pytest.fixture(scope="function", autouse=True)
    def funcion_auto(self):
        print("begin")
        yield
        print("end")

    def test_case1(self):
        print("test_case1:")
        assert 0 == 0

    def test_case2(self):
        print("test_case2:")
        assert 0 == 0
