# -*- coding: utf-8 -*-
# @Time    : 2019/8/15 0015 21:08
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : test_fixtureParams.py
# @Software: PyCharm


import uuid
import pytest



def duuid():
    return str(uuid.uuid4())

duuids=[]
duuids.append(duuid())

@pytest.fixture(scope="function", params=duuids)
def gparams(request):
    p = request.param
    return p


def guuid():
    def _uuid():
        return str(uuid.uuid4())
    return _uuid

@pytest.fixture(scope="function", params=[guuid()])
def funcparam(request):
    p = request.param
    return p()

@pytest.fixture(scope="function", params=[guuid(), guuid()])
def funcparams(request):
    p = request.param
    return p()




def test_params1(gparams):
    print("test_params1:"+gparams)
    #fb3dc70e-273f-4622-bedb-72b3967e9296

def test_params1_1(gparams):
    print("test_params1_1:"+gparams)
    #fb3dc70e-273f-4622-bedb-72b3967e9296

def test_params2(funcparam):
    print("test_params2:"+funcparam)
    #92bc5bf6-0dbe-44d0-b402-29f57971949e

def test_params2_2(funcparam):
    print("test_params2:" + funcparam)
    #2d42e226-47f1-47d5-9561-557ab2a1115e

def test_params3(funcparams):
    print("test_params3:"+funcparams)
    #05e9e475-fb6e-4a02-8f47-dd14bdea53f4
    #520bd717-7d95-4281-94f7-d7ba45f88db1