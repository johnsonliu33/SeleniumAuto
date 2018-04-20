__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_getWebElementAttribute(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        searchBox = self.driver.find_element_by_id('query')
        print(searchBox.get_attribute('name'))
        searchBox.send_keys('测试工程师指定的输入内容')
        print(searchBox.get_attribute('value'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()