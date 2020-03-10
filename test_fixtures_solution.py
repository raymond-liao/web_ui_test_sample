# -*- coding: utf-8 -*-
# Created at 03/09/2020

__author__ = 'raniys'

import pytest


# Implement the fixture that has module scope
@pytest.fixture(scope='module')
def resource_1_setup(request):
    print('\nSetup for resource 1 called')

    def resource_1_teardown():
        print('\nTeardown for resource 1 called')

    # An alternative option for executing teardown code is to make use of the addfinalizer method of the request-context
    # object to register finalization functions.
    # Source - https://docs.pytest.org/en/latest/fixture.html
    request.addfinalizer(resource_1_teardown)


@pytest.mark.sample
def test_1_using_resource_1(resource_1_setup):
    print('Test 1 uses resource 1')


@pytest.mark.sample
def test_2_not_using_resource_1():
    print('\n Test 2 does not need Resource 1')
