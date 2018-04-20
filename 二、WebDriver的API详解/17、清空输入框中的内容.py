__author = 'Robin'

from selenium import webdriver
import unittest
import time


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_clearInputBoxText(self):
        url = 'http://www.baidu.com'
        self.driver.get(url)
        input = self.driver.find_element_by_id('kw')
        input.send_keys('光荣之路自动化测试')
        time.sleep(3)
        input.clear()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()