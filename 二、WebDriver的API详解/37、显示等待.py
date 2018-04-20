__author = 'Robin'

from selenium import webdriver
import unittest
import traceback
from selenium.webdriver.common.by import By
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.common.exceptions import TimeoutException,NoSuchElementException


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_explicitWait(self):
        url = 'F:\\HTMLTest\\37.html'
        self.driver.get(url)
        try:
            wait = WebDriverWait(self.driver,10,0.2)
            wait.until(EC.title_is('你喜欢的水果'))
            print('网页标题是“你喜欢的水果”')
            element = WebDriverWait(self.driver,10).until(lambda x:x.find_element_by_xpath("//input[@value='Display alert box']"))
            element.click()
            alert = wait.until(EC.alert_is_present())
            print(alert.text)
            alert.accept()
            peach = self.driver.find_element_by_id('peach')
            peachElement = wait.until(EC.element_to_be_selected(peach))
            print('下拉框列表的选项‘桃子’目前处在选中状态')
            wait.until(EC.element_to_be_clickable((By.ID,'check')))
            print('复选框可见并且能被单击')
        except TimeoutException as e:
            print(traceback.print_exc())
        except NoSuchElementException as e:
            print(traceback.print_exc())
        except Exception as e:
            print(traceback.print_exc())
    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()