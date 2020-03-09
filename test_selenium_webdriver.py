# -*- coding: utf-8 -*-
# Created at 03/09/2020

__author__ = 'raniys'

import pytest
import pytest_html
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.keys import Keys
from time import sleep


# Fixture for Firefox
@pytest.fixture(scope="class")
def driver_init(request):
    ff_driver = webdriver.Firefox()
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


# Fixture for Chrome
@pytest.fixture(scope="class")
def chrome_driver_init(request):
    chrome_driver = webdriver.Chrome()
    request.cls.driver = chrome_driver
    yield
    chrome_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


class TestURL(BasicTest):
    def test_open_url(self):
        self.driver.get("https://www.baidu.com/")
        print(self.driver.title)

        sleep(5)


@pytest.mark.usefixtures("chrome_driver_init")
class BasicChromeTest:
    pass


class TestURLChrome(BasicChromeTest):
    def test_open_url(self):
        self.driver.get("https://www.baidu.com/")
        print(self.driver.title)

        sleep(5)
