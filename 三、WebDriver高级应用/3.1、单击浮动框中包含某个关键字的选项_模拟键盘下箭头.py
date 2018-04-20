__author = 'Robin'

from selenium import webdriver
import unittest
import time
from selenium.webdriver.common.keys import Keys


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_visitSogou(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        searchBox = self.driver.find_element_by_id('query')
        searchBox.send_keys('光荣之路')
        time.sleep(2)
        for i in range(3):
            searchBox.send_keys(Keys.DOWN)
            time.sleep(1)
        searchBox.send_keys(Keys.ENTER)
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()