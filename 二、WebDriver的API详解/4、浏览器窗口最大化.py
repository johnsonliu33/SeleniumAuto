__author = 'Robin'

from selenium import webdriver
import unittest

# 运行报错，解决方法：更新谷歌浏览器驱动到最新版本即可
class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_maximizeWindow(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        self.driver.maximize_window()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()