# -*- coding: utf-8 -*-
# @Time    : 2019/10/29 15:15
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : caplogtest.py
# @Software: PyCharm
import logging

class TestClass(object):


    def test_one(self,caplog):
        logger = logging.getLogger(__name__)
        logger.info('spam')
        logger.warning('eggs')
        logger.error('bacon')

        x = "this"
        assert 'i' in x