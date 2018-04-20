__author = 'Robin'

from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import NoSuchElementException
import traceback


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_visitSogou(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        try:
            searchBox = self.driver.find_element_by_id('query')
            searchBox.send_keys('光荣之路')
            time.sleep(2)
            suggetion_option = self.driver.find_element_by_xpath("//ul/li[contains(.,'电影')]")
            suggetion_option.click()
            time.sleep(3)
        except NoSuchElementException as e:
            print(traceback.print_exc())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()