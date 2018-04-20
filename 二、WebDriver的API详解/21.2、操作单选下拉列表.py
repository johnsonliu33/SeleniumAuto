__author = 'Robin'

from selenium import webdriver
import unittest
import time
from selenium.webdriver.support.ui import Select


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_operateDropList(self):
        url = 'F:\\HTMLTest\\selectText.html'
        self.driver.get(url)
        select_element = Select(self.driver.find_element_by_xpath('//select'))
        print(select_element.first_selected_option.text)
        all_options = select_element.options
        print(len(all_options))
        if all_options[1].is_enabled() and not all_options[1].is_selected():
            select_element.select_by_index(1)
            print(select_element.all_selected_options[0].text)
            self.assertEqual(select_element.all_selected_options[0].text,'西瓜')
        time.sleep(2)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()