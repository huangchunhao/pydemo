# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 0013 20:29
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : test_sample.py.py
# @Software: PyCharm

import logging
logger = logging.getLogger(__name__)

def func(x):
    return x+1


def test_answer(something):
    logger.info('13:{}'.format("4455"))
    assert func(3)==4