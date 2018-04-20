__author = 'Robin'

from selenium import webdriver
import unittest
import time


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_clickButton(self):
        url = 'F:\\HTMLTest\\clickButton.html'
        self.driver.get(url)
        button = self.driver.find_element_by_id('button')
        button.click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()