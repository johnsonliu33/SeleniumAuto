__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_window_size(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        sizeDict = self.driver.get_window_size()
        print('当前浏览器窗口的宽：',sizeDict['width'])
        print('当前浏览器窗口的高：',sizeDict['height'])
        self.driver.set_window_size(width=200,height=400,windowHandle='current')
        print(self.driver.get_window_size(windowHandle='current'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()