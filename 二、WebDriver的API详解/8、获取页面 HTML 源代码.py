__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_getPageSource(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        pageSource = self.driver.page_source
        print(pageSource)
        self.assertTrue('新闻'in pageSource,"页面源代码中未找到'新闻'关键字")

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()