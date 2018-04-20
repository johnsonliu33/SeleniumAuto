__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
import time


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_dragPageElement(self):
        url = 'http://jqueryui.com/resources/demos/draggable/scroll.html'
        self.driver.get(url)
        initialPosition = self.driver.find_element_by_id('draggable')
        targetPosition = self.driver.find_element_by_id('draggable2')
        dragElement = self.driver.find_element_by_id('draggable3')
        action_chains = ActionChains(self.driver)
        action_chains.drag_and_drop(initialPosition,targetPosition).perform()
        for i in range(5):
            action_chains.drag_and_drop_by_offset(dragElement,10,10).perform()
            time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()