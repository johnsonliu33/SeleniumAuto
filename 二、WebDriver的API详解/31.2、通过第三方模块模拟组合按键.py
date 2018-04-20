__author = 'Robin'

from selenium import webdriver
import unittest
import win32api
import win32con
import time

VK_CODE = {
        'enter':0x0D,
        'Ctrl':0x11,
        'A':0x41,
        'V':0x56,
        'X':0x58
    }

def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName],0,0,0)

def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName],0,win32con.KEYEVENTF_KEYUP,0)

class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_simulationCombinationKeys(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        searchBox = self.driver.find_element_by_id('query')
        searchBox.click()
        searchBox.send_keys('光荣之路自动化测试')
        time.sleep(3)
        keyDown('Ctrl')
        keyDown('A')

        keyUp('A')
        keyUp('Ctrl')

        keyDown('Ctrl')
        keyDown('X')

        keyUp('X')
        keyUp('Ctrl')

        self.driver.get('http://www.baidu.com')
        self.driver.find_element_by_id('kw').click()
        keyDown('Ctrl')
        keyDown('V')

        keyUp('V')
        keyUp('Ctrl')

        keyDown('enter')
        keyUp('enter')

        time.sleep(5)


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()