# -*- coding: utf-8 -*-
# @Time    : 2019/8/13 0013 20:52
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : calling.py
# @Software: PyCharm
import pytest

#在本文件的同级路径下执行命令python calling.py即可执行测试

if __name__=="__main__":
    pytest.main(['-x', './test'])#这里还指出命令行参数 和 pytest的执行参数
