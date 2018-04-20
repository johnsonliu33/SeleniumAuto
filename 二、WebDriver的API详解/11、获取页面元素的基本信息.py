__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_getBasicInfo(self):
        url = 'http://www.baidu.com'
        self.driver.get(url)
        newsElement = self.driver.find_element_by_xpath("//a[text()='新闻']")
        print('元素的标签名：',newsElement.tag_name)
        print('元素的 size:',newsElement.size)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()