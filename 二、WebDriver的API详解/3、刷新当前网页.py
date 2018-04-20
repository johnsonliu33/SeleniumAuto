__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_refreshCurrentPage(self):
        url='http://www.sogou.com'
        self.driver.refresh()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()