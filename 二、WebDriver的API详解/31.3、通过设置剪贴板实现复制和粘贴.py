__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.webdriver import ActionChains
from selenium.webdriver.common.keys import Keys
import win32clipboard as w
import win32con
import time

def getText():
    w.OpenClipboard()
    d = w.GetClipboardData(win32con.CF_TEXT)
    w.CloseClipboard()
    return d

def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT,aString)
    w.CloseClipboard()

class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_copyAndPaste(self):
        url = 'http://www.baidu.com'
        self.driver.get(url)
        content = '光荣之路'
        setText(content)
        getContent = getText()
        print(getContent)
        self.driver.find_element_by_id('kw').click()
        ActionChains(self.driver).key_down(Keys.CONTROL).send_keys('v').key_up(Keys.CONTROL).perform()
        self.driver.find_element_by_id('su').click()
        time.sleep(3)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()