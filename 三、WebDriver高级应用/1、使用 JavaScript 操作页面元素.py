__author = 'Robin'

from selenium import webdriver
import unittest
import time
import traceback
from selenium.common.exceptions import WebDriverException


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_executeScript(self):
        url = 'http://www.baidu.com'
        self.driver.get(url)
        searchInputBoxJS="document.getElementById('kw').value='光荣之路';"
        searchButtonJS = "document.getElementById('su').click()"
        try:
            self.driver.execute_script(searchInputBoxJS)
            time.sleep(2)
            self.driver.execute_script(searchButtonJS)
            time.sleep(2)
            self.assertTrue('百度百科'in self.driver.page_source)
        except WebDriverException as e:
            print('在页面中没有找到操作的页面元素',traceback.print_exc())
        except AssertionError as e:
            print('页面不存在断言的关键字串')
        except Exception as e:
            print(traceback.print_exc())

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()