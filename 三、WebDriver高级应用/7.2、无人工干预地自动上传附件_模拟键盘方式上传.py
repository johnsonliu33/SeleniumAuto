# -*- coding: utf-8 -*-
# @Time    : 2018/4/16 18:48
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : 7.1、无人工干预地自动上传附件_使用send方式上传.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import TimeoutException,NoSuchAttributeException
import traceback
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.common.by import By
from selenium.webdriver.support import expected_conditions as EC
import win32api
import win32con
import win32clipboard as w


def setText(aString):
    w.OpenClipboard()
    w.EmptyClipboard()
    w.SetClipboardData(win32con.CF_UNICODETEXT,aString)
    w.CloseClipboard()

VK_CODE ={
    'enter':0x0D,
    'ctrl':0x11,
    'v':0x56
}


def keyDown(keyname):
    win32api.keybd_event(VK_CODE[keyname],0,0,0)


def keyUp(keyname):
    win32api.keybd_event(VK_CODE[keyname],0,win32con.KEYEVENTF_KEYUP,0)


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_uploadFileByKeyboard(self):
        url = 'D:\\HtmlTest\\test_07.html'
        self.driver.get(url)
        try:
            wait = WebDriverWait(self.driver,10,0.2)
            wait.until(EC.element_to_be_clickable((By.ID,'file')))
        except TimeoutException as e:
            print(traceback.print_exc())
        except NoSuchAttributeException as e:
            print(traceback.print_exc())
        except Exception as e:
            print(traceback.print_exc())
        else:
            setText("D:\\TestFile\\test.txt")
            self.driver.find_element_by_id('file').click()
            time.sleep(2)
            keyDown('ctrl')
            keyDown('v')
            keyUp('v')
            keyUp('ctrl')
            time.sleep(1)
            keyDown('enter')
            keyUp('enter')
            time.sleep(2)
            fileSubmitButton = self.driver.find_element_by_id('filesubmit')
            fileSubmitButton.click()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()


