__author = 'Robin'

from selenium import webdriver
import unittest

class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_visitSogou(self):
        self.driver.get('http://www.sogou.com')
        print(self.driver.current_url)

    def tearDown(self):
        self.driver.quit()

if __name__ =='__main__':
    unittest.main()