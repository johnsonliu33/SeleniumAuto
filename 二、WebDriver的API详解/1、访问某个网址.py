__author = 'Robin'

from selenium import webdriver
import unittest

class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_visitSogou(self):
        visit_url = 'http://www.sogou.com'
        self.driver.get(visit_url)
        assert self.driver.title.find('搜狗搜索引擎')>=0,'assert error'

    def tearDown(self):
        self.driver.quit()

if __name__ =='__main__':
    unittest.main()