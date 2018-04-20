# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 19:35
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : 7.3、无人工干预地自动上传附件_使用第三方工具方式上传.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time,os
import traceback
from selenium.common.exceptions import TimeoutException,NoSuchAttributeException
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_uploadFileByAutoIt(self):
        url = 'D:\\HtmlTest\\test_07.html'
        self.driver.get(url)
        try:
            wait = WebDriverWait(self.driver,10,0.2)
            wait.until(EC.element_to_be_clickable((By.ID,'file')))
        except TimeoutException as e:
            print(traceback.print_exc())
        else:
            self.driver.find_element_by_id('file').click()
            os.system('D:\\TestFile\\test.exe')
            time.sleep(5)
            fileSubmitButton = self.driver.find_element_by_id('filesubmit')
            fileSubmitButton.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


