__author = 'Robin'

from selenium import webdriver
import unittest
import time


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_printSelectText(self):
        url = 'F:\\HTMLTest\\selectText.html'
        self.driver.get(url)
        select = self.driver.find_element_by_name('fruit')
        all_options = select.find_elements_by_tag_name('option')
        for option in all_options:
            print('选项显示的文本：',option.text)
            print('选项值为：',option.get_attribute('value'))
            option.click()
            time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()