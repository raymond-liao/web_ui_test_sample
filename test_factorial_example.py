# -*- coding: utf-8 -*-
# Created at 03/09/2020

__author__ = 'raniys'

import math

import pytest

from factorial_example import factorial_function


@pytest.mark.sample
def test_factorial_functionality():
    print("Inside test_factorial_functionality")

    assert factorial_function(0) == 1
    assert factorial_function(4) == 24


@pytest.mark.sample
def test_standard_library():
    print("Inside test_standard_library")

    for i in range(5):
        # verify whether factorial is calculated correctly
        # by checking against result against  standard
        # library - math.factorial()
        assert math.factorial(i) == factorial_function(i)


@pytest.mark.sample
def test_negative_number():
    print("Inside test_negative_number")

    # This test case would pass if Assertion Error
    # is raised. In this case, the input number is negative
    # hence, the test case passes
    with pytest.raises(AssertionError):
        factorial_function(-10)
