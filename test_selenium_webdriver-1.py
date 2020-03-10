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
@pytest.fixture(params=["chrome", "firefox"], scope="class")
def driver_init(request):
    if request.param == "chrome":
        web_driver = webdriver.Chrome()
    if request.param == "firefox":
        web_driver = webdriver.Firefox()
    request.cls.driver = web_driver
    yield
    web_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


@pytest.mark.smoke
class TestURL(BasicTest):
    def test_open_url(self):
        self.driver.get("https://www.patballoon.com/")
        print(self.driver.title)

        sleep(5)
