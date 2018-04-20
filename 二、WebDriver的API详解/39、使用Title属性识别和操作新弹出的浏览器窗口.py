__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.common.exceptions import NoSuchElementException,TimeoutException
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
import traceback
import time


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_identifyPopUpWindowByTitle(self):
        url = 'F:\\HTMLTest\\39.html'
        self.driver.get(url)
        WebDriverWait(self.driver,10,0.2).until(EC.element_to_be_clickable((By.LINK_TEXT,'sogou 搜索'))).click()
        all_handles=self.driver.window_handles
        print(self.driver.current_window_handle)
        print(len(all_handles))
        time.sleep(2)
        if len(all_handles)>0:
            try:
                for windowHandle in all_handles:
                    self.driver.switch_to.window(windowHandle)
                    print(self.driver.title)
                    if self.driver.title =='搜狗搜索引擎 - 上网从搜狗开始':
                        WebDriverWait(self.driver,10,0.2).until(lambda x:x.find_element_by_id('query')).send_keys('sogou 首页的浏览器窗口被找到')
                        time.sleep(2)
            except NoSuchElementException as e:
                print(traceback.print_exc())
            except TimeoutException as e:
                print(traceback.print_exc())
        self.driver.switch_to.window(all_handles[0])
        print(self.driver.title)
        self.assertEqual(self.driver.title,'你喜欢的水果')

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()