__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
import time


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_roverOnElement(self):
        url = 'F:\\HTMLTest\\34.html'
        self.driver.get(url)
        link1 = self.driver.find_element_by_link_text('鼠标指过来1')
        link2 = self.driver.find_element_by_link_text('鼠标指过来2')
        p = self.driver.find_element_by_xpath('//p')
        print(link1.text,link2.text)
        ActionChains(self.driver).move_to_element(link1).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(p).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(link2).perform()
        time.sleep(2)
        ActionChains(self.driver).move_to_element(p).perform()
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()