# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 15:31
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : test_mark.py
# @Software: PyCharm

import pytest
#官网例子
@pytest.mark.parametrize("test_input,expected"
    ,[("3+5", 8), ("2+4", 6),
      pytest.param("6*9", 42, marks=pytest.mark.xfail)],)
def test_eval(test_input, expected):
    assert eval(test_input) == expected


#PASSED test_mark.py::test_eval[3+5-8]
#PASSED test_mark.py::test_eval[2+4-6]
#XFAIL test_mark.py::test_eval[6*9-42]


