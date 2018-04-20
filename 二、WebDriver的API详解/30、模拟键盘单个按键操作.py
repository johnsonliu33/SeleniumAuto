__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.webdriver.common.keys import Keys
import time


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_simulateASingleKeys(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        query = self.driver.find_element_by_id('query')
        query.send_keys(Keys.F12)
        time.sleep(3)
        query.send_keys(Keys.F12)
        query.send_keys('selenium')
        query.send_keys(Keys.ENTER)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()