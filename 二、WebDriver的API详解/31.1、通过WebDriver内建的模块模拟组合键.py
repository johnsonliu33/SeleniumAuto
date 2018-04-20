__author = 'Robin'

from selenium import webdriver
import unittest
import time
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_simulationCombinationKeys(self):
        url = 'http://www.baidu.com'
        self.driver.get(url)
        input = self.driver.find_element_by_id('kw')
        input.click()
        input.send_keys('光荣之路')
        time.sleep(2)
        action_chain = ActionChains(self.driver)
        action_chain.key_down(Keys.CONTROL).send_keys('a').key_up(Keys.CONTROL).perform()
        time.sleep(2)
        action_chain.key_down(Keys.CONTROL).send_keys('x').key_up(Keys.CONTROL).perform()
        self.driver.get(url)
        self.driver.find_element_by_id('kw').click()
        action_chain.key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()