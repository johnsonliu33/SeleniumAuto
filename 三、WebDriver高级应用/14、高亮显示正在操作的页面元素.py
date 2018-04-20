# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 15:26
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : 14、高亮显示正在操作的页面元素.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time
import traceback

def highLightElement(driver,element):
    driver.execute_script("arguments[0].setAttribute('style',arguments[1]);",element,"background:green;border:2px solid red;")

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_highLightWebElement(self):
        url = 'http://www.sogou.com'
        self.driver.maximize_window()
        self.driver.get(url)

        searchBox = self.driver.find_element_by_id('query')
        highLightElement(self.driver,searchBox)
        time.sleep(3)
        searchBox.send_keys('光荣之路自动化测试')

        submitButton = self.driver.find_element_by_id('stb')
        highLightElement(self.driver,submitButton)
        time.sleep(3)
        submitButton.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()