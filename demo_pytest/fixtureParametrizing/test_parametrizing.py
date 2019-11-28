# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 13:54
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : test_parametrizing.py
# @Software: PyCharm
import pytest

seq=["case1","case2","case3","cas5"]


# @pytest.fixture(scope="module",params=seq)
# def params(request):
#     return request.param
#
#
#
# def test_params(params):
#     print(params)
#     assert "case" in params


##ids中的值 只是一种对应关系  ，实际使用的值还是seq中的值
##ids可以是描述
@pytest.fixture(scope="module",params=seq,ids=["test1","test2","test3","错误"])
def ids(request):
    return request.param

def test_ids(ids):
    print(ids)
    assert "case" in ids
