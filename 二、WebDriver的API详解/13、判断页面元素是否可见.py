__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_getElementIsDisplay(self):
        url = 'F:\\HTMLTest\\webElementIsDisplayed.html'
        self.driver.get(url)
        div2 = self.driver.find_element_by_id('div2')
        print(div2.is_displayed())
        self.driver.find_element_by_id('button1').click()
        print(div2.is_displayed())
        div4 =self.driver.find_element_by_id('div4')
        print(div4.is_displayed())
        self.driver.find_element_by_id('button2').click()
        print(div4.is_displayed())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()