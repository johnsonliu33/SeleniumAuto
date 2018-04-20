# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 18:34
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : SoGou.py
# @Software: PyCharm

from selenium import webdriver
import unittest
from LogTest import *


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_visitSogou(self):
        info('============================== 搜索 =========================')
        url = 'http://www.sogou.com'
        self.driver.get(url)
        self.driver.find_element_by_id('query').send_keys('光荣之路自动化测试')
        info("在输入框中输入搜索关键字串'光荣之路自动化测试'")
        self.driver.find_element_by_id('stb').click()
        info('单击搜索按钮')
        info('======================== 测试用例执行结束 =====================')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


