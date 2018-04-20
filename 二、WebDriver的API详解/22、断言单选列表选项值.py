__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_checkSelectText(self):
        url = 'F:\\HTMLTest\\selectText.html'
        self.driver.get(url)
        select_element = Select(self.driver.find_element_by_xpath('//select'))
        actual_options = select_element.options
        expect_optionList = ['桃子','西瓜','橘子','猕猴桃','山楂','荔枝']
        actual_optionsList = list(map(lambda option:option.text,actual_options))
        self.assertListEqual(expect_optionList,actual_optionsList)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()