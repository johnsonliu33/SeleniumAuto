__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_window_position(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        position = self.driver.get_window_position()
        print('当前浏览器所在位置的横坐标：',position['x'])
        print('当前浏览器所在位置的纵坐标：',position['y'])
        self.driver.set_window_position(y=200,x=400)
        print(self.driver.get_window_position())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()