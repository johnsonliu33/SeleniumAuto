# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 20:23
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : 8、右键另存为下载文件.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time,os
from selenium.webdriver.common.keys import Keys
from selenium.webdriver import ActionChains
import traceback
import win32api
import win32con


VK_CODE = {'enter':0x0D,'down_arrow':0x28}


def keyDown(keyname):
    win32api.keybd_event(VK_CODE[keyname],0,0,0)


def keyUp(keyname):
    win32api.keybd_event(VK_CODE[keyname],0,win32con.KEYEVENTF_KEYUP,0)


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_visitSogou(self):
        url = 'http://ftp.mozilla.org/pub/mozilla.org//firefox/releases/35.0b8/win32/zh-CN/'
        self.driver.get(url)
        self.driver.maximize_window()
        time.sleep(5)
        a = self.driver.find_element_by_link_text('Firefox Setup 35.0b8.exe')
        time.sleep(2)
        ActionChains(self.driver).context_click(a).perform()
        time.sleep(2)
        for i in range(4):
            a.send_keys(Keys.DOWN)
            keyDown('down_arrow')
            keyUp('down_arrow')
            print(i)
            time.sleep(2)
        time.sleep(2)
        keyDown('enter')
        keyUp('enter')
        time.sleep(3)
        os.system('D:\\iDownload\\loadFile.exe')
        time.sleep(100)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


