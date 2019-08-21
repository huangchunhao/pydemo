# -*- coding: utf-8 -*-
# @Time    : 2019/8/21 0021 21:40
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : school.py
# @Software: PyCharm
class School():
    def __init__(self, name, address):
        self.name = name
        self.address = address
        # self.common = common

    def setinfo(self, info):
        self.name, self.address = info

    def getinfo(self):
        return self.name, self.address

    def delinfo(self):
        self.name, self.address = 0, 0

    @property
    def common(self):
        return self._common

    @common.setter #一定要在前面定义了common的@property，才能使用@common.setter
    def common(self, common):
        self._common = common

    info = property(getinfo, setinfo, delinfo, "信息")#这里getinfo一定要放在最前面
    # common = property(setCommon)
