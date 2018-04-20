__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
import time


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_visitSogou(self):
        url = 'F:\\HTMLTest\\33.html'
        self.driver.get(url)
        div = self.driver.find_element_by_id('div1')
        ActionChains(self.driver).click_and_hold(div).perform()
        time.sleep(2)
        ActionChains(self.driver).release(div).perform()
        time.sleep(2)
        ActionChains(self.driver).click_and_hold(div).perform()
        time.sleep(2)
        ActionChains(self.driver).release(div).perform()


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()