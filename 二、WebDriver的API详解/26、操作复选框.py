__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_operateCheckBox(self):
        url = 'F:\\HTMLTest\\26.html'
        self.driver.get(url)
        berryCheckBox = self.driver.find_element_by_xpath("//input[@value='berry']")
        berryCheckBox.click()
        self.assertTrue(berryCheckBox.is_selected(),'草莓复选框未被选中！')
        if berryCheckBox.is_selected():
            berryCheckBox.click()
            self.assertFalse(berryCheckBox.is_selected())
        checkBoxList = self.driver.find_elements_by_xpath("//input[@name='fruit']")
        for box in checkBoxList:
            if not box.is_selected():
                box.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()