__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.common.exceptions import TimeoutException
from selenium.webdriver.common.keys import Keys
import time


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_pageLoadTime(self):
        url = 'http://mail.163.com'
        self.driver.set_page_load_timeout(4)
        self.driver.maximize_window()
        try:
            startTime = time.time()
            self.driver.get(url)
        except TimeoutException:
            self.driver.execute_script('window.stop()')
        end = time.time()- startTime
        print(end)
        self.driver.switch_to.frame('x-URS-iframe')
        userName = self.driver.find_element_by_xpath('//input[@name="email"]')
        userName.send_keys('liqinjia372135')
        pwd = self.driver.find_element_by_xpath('//input[@name="password"]')
        pwd.send_keys('lqj372135094')
        pwd.send_keys(Keys.RETURN)

        self.driver.get(url)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()