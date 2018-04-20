__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException,TimeoutException
import traceback


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_implicitlyWait(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        try:
            searchBox = self.driver.find_element_by_id('query')
            searchBox.send_keys('光荣之路自动化测试')
            click = self.driver.find_element_by_id('stb')
            click.click()
        except (NoSuchElementException,TimeoutException) as e:
            traceback.print_exc()
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()