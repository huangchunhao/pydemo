# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 8:44
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : test_class.py
# @Software: PyCharm
class Test_for_pytest_scope(object):
    def test_case_p1(self, test_module, test_class, test_function, test_session, test_package):
        print("testcase/package/test_class_p.py-test_case_p1||" + test_function)
        print("testcase/package/test_class_p.py-test_case_p1||" + test_module)
        print("testcase/package/test_class_p.py-test_case_p1||" + test_class)
        print("testcase/package/test_class_p.py-test_case_p1||" + test_session)
        print("testcase/package/test_class_p.py-test_case_p1||" + test_package)

    def test_case_p2(self, test_module, test_class, test_function, test_session, test_package):
        print("testcase/package/test_class_p.py-test_case_p2||" + test_function)
        print("testcase/package/test_class_p.py-test_case_p2||" + test_module)
        print("testcase/package/test_class_p.py-test_case_p2||" + test_class)
        print("testcase/package/test_class_p.py-test_case_p2||" + test_session)
        print("testcase/package/test_class_p.py-test_case_p2||" + test_package)


def test_m_p1_inclass(test_module, test_class, test_function, test_session, test_package):
    print("testcase/package/test_class_p.py-test_m_p1_inclass||" + test_function)
    print("testcase/package/test_class_p.py-test_m_p1_inclass||" + test_module)
    print("testcase/package/test_class_p.py-test_m_p1_inclass||" + test_class)
    print("testcase/package/test_class_p.py-test_m_p1_inclass||" + test_session)
    print("testcase/package/test_class_p.py-test_m_p1_inclass||" + test_package)


def test_m_p2_inclass(test_module, test_class, test_function, test_session, test_package):
    print("testcase/package/test_class_p.py-test_m_p2_inclass||" + test_function)
    print("testcase/package/test_class_p.py-test_m_p2_inclass||" + test_module)
    print("testcase/package/test_class_p.py-test_m_p2_inclass||" + test_class)
    print("testcase/package/test_class_p.py-test_m_p2_inclass||" + test_session)
    print("testcase/package/test_class_p.py-test_m_p2_inclass||" + test_package)