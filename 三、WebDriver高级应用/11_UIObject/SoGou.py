# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 9:52
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : SoGou.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException
import traceback
from ObjectMap import ObjectMap


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.obj = ObjectMap()
        self.driver = webdriver.Chrome()

    def test_soGouSearch(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        try:
            searchBox = self.obj.getElementObject(self.driver,'sogou','searchBox')
            searchBox.send_keys('WebDriver 实战宝典')
            searchButton = self.obj.getElementObject(self.driver,'sogou','searchButton')
            searchButton.click()
            time.sleep(2)
            self.assertTrue('吴晓华' in self.driver.page_source,'assert error!')
        except Exception as e:
            print(traceback.print_exc())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()