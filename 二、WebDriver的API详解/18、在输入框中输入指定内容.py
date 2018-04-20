__author = 'Robin'

from selenium import webdriver
import unittest
import time


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_sendTextToInputBoxText(self):
        url = 'F:\\HTMLTest\\sendTextToInputBoxText.html'
        self.driver.get(url)
        input = self.driver.find_element_by_id('text')
        input.clear()
        input.send_keys('我是输入的文本内容')
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()