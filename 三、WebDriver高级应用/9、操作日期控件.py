# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 21:09
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : 9、操作日期控件.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time,traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_datePicker(self):
        url = 'http://jqueryui.com/resources/demos/datepicker/other-months.html'
        self.driver.get(url)
        try:
            wait = WebDriverWait(self.driver,10,0.2)
            wait.until(EC.element_to_be_clickable((By.ID,'datepicker')))
        except TimeoutException as e:
            print(traceback.print_exc())
        except Exception as e:
            print(traceback.print_exc())
        except NoSuchElementException as e:
            print(traceback.print_exc())
        else:
            dateInputBox = self.driver.find_element_by_id('datepicker')
            dateInputBox.send_keys('14/04/2018')
            time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


