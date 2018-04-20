__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
import win32clipboard as w
import win32con
import time

def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT,aString)
    w.CloseClipboard()

class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_rightClickMouse(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        searchBox = self.driver.find_element_by_id('query')
        searchBox.click()
        time.sleep(2)

        ActionChains(self.driver).context_click(searchBox).perform()
        setText('gloryroad')
        time.sleep(2)
        ActionChains(self.driver).send_keys("P").perform()
        time.sleep(2)
        self.driver.find_element_by_id('stb').click()
        time.sleep(2)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()