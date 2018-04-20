# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 15:38
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : 15、浏览器中新开标签页（Tab）.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time
import win32api,win32con

VK_CODE = {'ctrl':0x11,'t':0x54,'tab':0x09}

def keyDown(keyName):
    win32api.keybd_event(VK_CODE[keyName],0,0,0)

def keyUp(keyName):
    win32api.keybd_event(VK_CODE[keyName],0,win32con.KEYEVENTF_KEYUP,0)

def simulateKey(firstKey,secondKey):
    keyDown(firstKey)
    keyDown(secondKey)
    keyUp(secondKey)
    keyUp(firstKey)

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_newTab(self):
        time.sleep(3)
        for i in range(2):
            simulateKey('ctrl','t')
        simulateKey('ctrl','tab')
        url = 'http://www.sogou.com'
        self.driver.get(url)
        self.driver.find_element_by_id('query').send_keys('光荣之路')
        self.driver.find_element_by_id('stb').click()
        time.sleep(3)
        self.assertTrue('乔什' in self.driver.page_source)

        all_handles = self.driver.window_handles
        print(len(all_handles))
        self.driver.switch_to.window(all_handles[1])
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys('WebDriver 实战宝典')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.assertTrue('吴晓华' in self.driver.page_source)

        self.driver.switch_to.window(all_handles[2])
        self.driver.get("http://www.baidu.com")
        self.driver.find_element_by_id('kw').send_keys('selenium')
        self.driver.find_element_by_id('su').click()
        time.sleep(3)
        self.assertTrue('www.seleniumhq.org' in self.driver.page_source)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()