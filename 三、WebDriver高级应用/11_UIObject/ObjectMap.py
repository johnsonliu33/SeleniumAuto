# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 9:52
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : ObjectMap.py
# @Software: PyCharm

from selenium.webdriver.support.ui import WebDriverWait
import configparser
import os


class ObjectMap(object):
   def __init__(self):
       self.uiObjectMapPath = os.path.dirname(os.path.abspath(__file__))+'\\UiObjectMap.ini'
       print(self.uiObjectMapPath)

   def getElementObject(self,driver,webSiteName,elementName):
       try:
           cf = configparser.ConfigParser()
           cf.read(self.uiObjectMapPath)
           locators = cf.get(webSiteName,elementName).split('>')
           locatorMethod = locators[0]
           locatorExpression = locators[1]
           print(locatorMethod,locatorExpression)
           element = WebDriverWait(driver,10).until(lambda x:x.find_element(locatorMethod,locatorExpression))
       except Exception as e:
           raise e
       else:
           return element
