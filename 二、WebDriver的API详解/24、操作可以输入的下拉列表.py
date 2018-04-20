__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_operateMultipleDropList(self):
        url = 'F:\\HTMLTest\\24.html'
        self.driver.get(url)
        self.driver.find_element_by_id('select').clear()
        time.sleep(2)
        self.driver.find_element_by_id('select').send_keys('c',Keys.ARROW_DOWN)
        self.driver.find_element_by_id('select').send_keys(Keys.ARROW_DOWN)
        self.driver.find_element_by_id('select').send_keys(Keys.ENTER)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()