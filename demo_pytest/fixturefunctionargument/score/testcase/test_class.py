# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 8:44
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : test_class.py
# @Software: PyCharm
class Test_for_pytest_scope(object):
    def test_case1(self,test_module,test_class,test_function,test_session,test_package):
        print("testcase/test_class.py-test_case1||" + test_function)
        print("testcase/test_class.py-test_case1||"+test_module)
        print("testcase/test_class.py-test_case1||"+test_class)
        print("testcase/test_class.py-test_case1||" + test_session)
        print("testcase/test_class.py-test_case1||" + test_package)

    def test_case2(self,test_module,test_class,test_function,test_session,test_package):
        print("testcase/test_class.py-test_case2||" + test_function)
        print("testcase/test_class.py-test_case2||"+test_module)
        print("testcase/test_class.py-test_case2||"+test_class)
        print("testcase/test_class.py-test_case2||" + test_session)
        print("testcase/test_class.py-test_case2||" + test_package)