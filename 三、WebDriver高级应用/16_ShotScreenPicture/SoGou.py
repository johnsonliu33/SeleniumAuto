# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 16:12
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : SoGou.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time,os
from FileUtil import createDir
import traceback

picDir = createDir()
def takeScreenShot(driver,savePath,picName):
    picPath = os.path.join(savePath,str(picName)+'.png')
    try:
        driver.get_screenshot_as_file(picPath)
    except Exception as e:
        print(traceback.print_exc())

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_visitSogou(self):
        url = 'http://www.sogou.com'
        self.driver.maximize_window()
        self.driver.get(url)
        try:
            self.driver.find_element_by_id('query').send_keys('光荣之路自动化测试')
            self.driver.find_element_by_id('stb').click()
            time.sleep(3)
            self.assertTrue('事在人为' in self.driver.page_source,"'事在人为'关键字串在页面源代码中未找到")
        except AssertionError as e:
            takeScreenShot(self.driver,picDir,e)
        except Exception as e:
            print(traceback.print_exc())
            takeScreenShot(self.driver,picDir,e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()