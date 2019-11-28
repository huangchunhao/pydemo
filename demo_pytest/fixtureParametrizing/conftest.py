# -*- coding: utf-8 -*-
# @Time    : 2019/11/28 15:39
# @Author  : Vincent
# @Email   : Vincent@163.com
# @File    : conftest.py
# @Software: PyCharm
import pytest

import logging
logger = logging.getLogger(__name__)
def pytest_sessionstart(session):
    session.results = dict()
    session.failedinfos= dict()


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()
    setattr(item, "rep_" + result.when, result)
    if result.when == 'call':
        item.session.results[item] = result
        if(result.failed):
            item.session.failedinfos[item] = item.nodeid



def pytest_sessionfinish(session, exitstatus):
    print()
    print('run status code:', exitstatus)
    passed_amount = sum(1 for result in session.results.values() if result.passed)
    failed_amount = sum(1 for result in session.results.values() if result.failed)
    print(f'there are {passed_amount} passed and {failed_amount} failed tests')
    # for name in session.results.keys():
    #     logger.info(name)

    for key,value in session.failedinfos.items():
        logger.info("%%%%%%%%%%%%%%%%%%%%")
        logger.info(key)
        logger.info(value)
        logger.info("%%%%%%%%%%%%%%%%%%%%")


@pytest.fixture
def something(request):
    yield
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            logger.info("executing test failed:{}".format(request.node.nodeid))
            request.session.failedinfos[request] = request.node.nodeid
        elif request.node.rep_call.passed:
            logger.info("executing test passed:{}".format(request.node.nodeid))

