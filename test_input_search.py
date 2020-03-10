# -*- coding: utf-8 -*-
# Created at 03/10/2020

__author__ = 'raniys'

import pytest
from selenium import webdriver
from time import sleep

from selenium.webdriver.common.by import By
from selenium.webdriver.common.keys import Keys
from selenium.webdriver.support import expected_conditions
from selenium.webdriver.support.wait import WebDriverWait


@pytest.fixture(scope="class")
def driver_init(request):
    ff_driver = webdriver.Firefox()
    ff_driver.set_window_size(480, 800)
    request.cls.driver = ff_driver
    yield
    ff_driver.close()


@pytest.mark.usefixtures("driver_init")
class BasicTest:
    pass


@pytest.mark.search
class TestURL(BasicTest):
    def test_open_url(self):
        self.driver.get("https://www.python.org/")
        print(self.driver.title)
        assert "Python" in self.driver.title

        # 显式等待
        # wait = WebDriverWait(self.driver, 10)
        # elem = wait.until(expected_conditions.element_to_be_clickable((By.NAME, 'q')))

        # 隐式等待
        self.driver.implicitly_wait(10)

        elem = self.driver.find_element_by_name("q")
        elem.clear()
        elem.send_keys("pycon")
        elem.send_keys(Keys.RETURN)
        assert "No results found." not in self.driver.page_source
