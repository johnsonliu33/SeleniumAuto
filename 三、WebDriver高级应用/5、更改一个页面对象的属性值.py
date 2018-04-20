__author = 'Robin'

from selenium import webdriver
import unittest
import time
from selenium.common.exceptions import WebDriverException
import traceback

def addAttribute(driver,elementObj,attributeName,value):
    driver.execute_script("arguments[0].%s=arguments[1]"% attributeName,elementObj,value)

def setAttribute(driver,elementObj,attributeName,value):
    driver.execute_script("arguments[0].setAttribute(arguments[1],arguments[2])",elementObj,attributeName,value)

def getAttribute(elementObj,attributeName):
    return elementObj.get_attribute(attributeName)

def removeAttribute(driver,elementObj,attributeName):
    driver.execute_script("arguments[0].removeAttribute(arguments[1])",elementObj,attributeName)

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_visitSogou(self):
        url = 'F:\\HTMLTest\\test_05.html'
        self.driver.get(url)
        element = self.driver.find_element_by_xpath('//input')
        addAttribute(self.driver,element,'name','search')
        print("添加的新属性值%s='%s'"%('name',getAttribute(element,'name')))

        print("更改文本框中的内容前的内容： " ,getAttribute(element,'value'))
        setAttribute(self.driver,element,'value','这是更改后的文字内容')
        print("更改文本框中内容后的内容：",getAttribute(element,'value'))

        print("更改文本框标签中的size属性值： " ,getAttribute(element,'size'))
        setAttribute(self.driver,element,'size',20)
        print("更改文本框标签中的size属性值：",getAttribute(element,'size'))

        print("文本框value属性值： " ,getAttribute(element,'value'))
        removeAttribute(self.driver,element,'value')
        print("删除value属性值后value属性值：",getAttribute(element,'value'))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()