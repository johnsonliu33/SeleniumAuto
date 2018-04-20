__author = 'Robin'

from selenium import webdriver
import unittest
import time
from selenium.webdriver import ActionChains


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_visitSogou(self):
        url = 'F:\\HTMLTest\\doubleClick.html'
        self.driver.get(url)
        inputBox = self.driver.find_element_by_id('inputBox')
        action_chains = ActionChains(self.driver)
        action_chains.double_click(inputBox).perform()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()