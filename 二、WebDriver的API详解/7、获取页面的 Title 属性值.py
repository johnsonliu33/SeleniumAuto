__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_getTitle(self):
        url = 'http://www.baidu.com'
        self.driver.get(url)
        title = self.driver.title
        print('当前网页的 title 属性值为：',title)
        self.assertEqual(title,'百度一下，你就知道','页面 Title 属性值错误！')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()