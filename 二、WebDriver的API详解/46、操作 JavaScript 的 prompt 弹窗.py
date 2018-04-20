__author = 'Robin'

from selenium import webdriver
import unittest
import time
from selenium.webdriver import ActionChains


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_handlePrompt(self):
        url = 'F:\\HTMLTest\\46.html'
        self.driver.get(url)
        element = self.driver.find_element_by_id('button')
        element.click()
        time.sleep(1)
        alert = self.driver.switch_to.alert
        self.assertEqual('这是一个 prompt 弹出框',alert.text)
        time.sleep(3)
        # ActionChains(self.driver).context_click(alert).perform()
        # ActionChains(self.driver).send_keys('要想改变命运，必须每天学习2小时！').perform()
        alert.send_keys('要想改变命运，必须每天学习2小时！')
        time.sleep(4)
        alert.accept()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()