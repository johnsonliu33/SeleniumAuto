__author = 'Robin'

from selenium import webdriver
import unittest
import time


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_getWebElementText(self):
        url = 'http://www.baidu.com'
        self.driver.get(url)
        time.sleep(3)
        aElement = self.driver.find_element_by_xpath("//*[@class='mnav'][1]")
        a_text = aElement.text
        self.assertEqual(a_text,'新闻')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()