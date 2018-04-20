__author = 'Robin'

from selenium import webdriver
import unittest

class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_visitRecentURL(self):
        firstURL='http://www.sogou.com'
        secondURL='http://www.baidu.com'
        self.driver.get(firstURL)
        self.driver.get(secondURL)
        self.driver.back()
        self.driver.forward()

    def tearDown(self):
        self.driver.quit()

if __name__ =='__main__':
    unittest.main()