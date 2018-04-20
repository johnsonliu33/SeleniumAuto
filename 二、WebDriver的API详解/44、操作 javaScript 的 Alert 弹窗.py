__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.common.exceptions import NoAlertPresentException
import time



class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_handleAlert(self):
        url = 'F:\\HTMLTest\\44.html'
        self.driver.get(url)
        button = self.driver.find_element_by_id('button')
        button.click()
        try:
            alert = self.driver.switch_to.alert
            time.sleep(2)
            self.assertEqual(alert.text,'这是一个 alert 弹出框')
            alert.accept()
        except NoAlertPresentException as e:
            self.fail('尝试操作的 alert 框未被找到')
            print(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()