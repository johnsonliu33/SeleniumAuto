__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def isElementPresent(self,by,value):
        try:
            element = self.driver.find_element(by=by,value=value)
        except NoSuchElementException as e:
            print(e)
            return False
        else:
            return True

    def test_isElementPresent(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        res = self.isElementPresent('id','query')
        if res is True:
            print('所查找的元素存在于页面上！')
        else:
            print('页面中未找到所需要的页面元素！')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()