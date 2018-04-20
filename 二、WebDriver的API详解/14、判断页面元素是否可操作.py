__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_visitSogou(self):
        url = 'F:\\HTMLTest\\webElementIsEnable.html'
        self.driver.get(url)
        input1 = self.driver.find_element_by_xpath("//input[@id='input1']")
        print(input1.is_enabled())
        input2 = self.driver.find_element_by_xpath("//input[@id='input2']")
        print(input2.is_enabled())
        input3 = self.driver.find_element_by_xpath("//input[@id='input3']")
        print(input3.is_enabled())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()