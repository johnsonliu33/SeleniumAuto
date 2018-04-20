__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_operateRadio(self):
        url = 'F:\\HTMLTest\\25.html'
        self.driver.get(url)
        berryRadio = self.driver.find_element_by_xpath("//input[@value='berry']")
        berryRadio.click()
        self.assertTrue(berryRadio.is_selected(),'草莓单选框未被选中')
        if berryRadio.is_selected():
            watermelonRadio = self.driver.find_element_by_xpath("//input[@value='watermelon']")
            watermelonRadio.click()
            self.assertFalse(berryRadio.is_selected())
        radioList = self.driver.find_elements_by_xpath("//input[@name='fruit']")
        for radio in radioList:
            if radio.get_attribute('value') == 'orange':
                if not radio.is_selected():
                    radio.click()
                    self.assertEqual(radio.get_attribute('value'),'orange')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()