# -*- coding: utf-8 -*-
# @Time    : 2019/8/14 8:43
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : conftest.py.py
# @Software: PyCharm
import uuid
import pytest

@pytest.fixture(scope="module")
def test_module():
    return "module"+str(uuid.uuid4())

@pytest.fixture(scope="class")
def test_class():
    return "class"+str(uuid.uuid4())

@pytest.fixture(scope="function")
def test_function():
    return "function"+str(uuid.uuid4())

@pytest.fixture(scope="session")
def test_session():
    return "session"+str(uuid.uuid4())


@pytest.fixture(scope="package")
def test_package():
    return "package"+str(uuid.uuid4())
