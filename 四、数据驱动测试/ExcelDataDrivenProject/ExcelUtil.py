# -*- coding: utf-8 -*-
# @Time    : 2018/4/20 20:21
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : ExcelUtil.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException
import traceback


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_visitSogou(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


