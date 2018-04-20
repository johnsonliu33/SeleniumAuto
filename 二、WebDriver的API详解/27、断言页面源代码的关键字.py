__author = 'Robin'

from selenium import webdriver
import unittest
import time

class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_assertKeyWord(self):
        url = 'http://www.baidu.com'
        self.driver.get(url)
        self.driver.find_element_by_id('kw').send_keys('光荣之路自动化测试')
        self.driver.find_element_by_id('su').click()
        time.sleep(4)
        assert '首页 -- 光荣之路' in self.driver.page_source,'页面源码中不存在该关键字'

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()