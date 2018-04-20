__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.webdriver.support.ui import Select
import time


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_operateMultipleOptionDropList(self):
        url = 'F:\\HTMLTest\\select.html'
        self.driver.get(url)
        select_element = Select(self.driver.find_element_by_xpath('//select'))
        select_element.select_by_index(0)
        select_element.select_by_visible_text('山楂')
        select_element.select_by_value('mihoutao')
        for option in select_element.all_selected_options:
            print(option.text)
        select_element.deselect_all()
        time.sleep(2)
        print('---------------- 再次选中 3 个选项 ------------------')
        select_element.select_by_index(1)
        select_element.select_by_visible_text('荔枝')
        select_element.select_by_value('juzi')
        select_element.deselect_by_visible_text('荔枝')
        select_element.deselect_by_index(1)
        select_element.deselect_by_value('juzi')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()