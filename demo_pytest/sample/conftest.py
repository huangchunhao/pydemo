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


@pytest.hookimpl(tryfirst=True, hookwrapper=True)
def pytest_runtest_makereport(item, call):
    outcome = yield
    result = outcome.get_result()

    setattr(item, "rep_" + result.when, result)
    logger.info(")))))))))))))")
    logger.info(result.caplog)
    logger.info(item)
    logger.info(")))))))))))))")

    if result.when == 'call':
        item.session.results[item] = result


def pytest_sessionfinish(session, exitstatus):
    print()
    print('run status code:', exitstatus)
    passed_amount = sum(1 for result in session.results.values() if result.passed)
    failed_amount = sum(1 for result in session.results.values() if result.failed)
    print(f'there are {passed_amount} passed and {failed_amount} failed tests')
    for key, value in session.results.items():
        logger.info("===============")
        logger.info(key)
        logger.info(value)
        logger.info("===============")
    for name in session.results.keys():
        logger.info("+++++++++++++++++")
        logger.info(name)
        logger.info("+++++++++++++++++")

@pytest.fixture
def something(request):
    yield
    if request.node.rep_setup.failed:
        print("setting up a test failed!", request.node.nodeid)
    elif request.node.rep_setup.passed:
        if request.node.rep_call.failed:
            print("executing test failed", request.node.nodeid)
        elif request.node.rep_call.passed:
            logger.info("executing test passed:{}".format(request.node.nodeid))
