__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_getCurrentPageURL(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        currentPageURL = self.driver.current_url
        print(currentPageURL)
        self.assertEqual(currentPageURL,'https://www.sogou.com/','当前网页网址非预期')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()