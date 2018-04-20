# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 10:45
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : 12.1、操作富文本框.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time,traceback
from selenium.common.exceptions import TimeoutException,NoSuchElementException
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.common.by import By


class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_sohuMailEmail(self):
        url = 'http://mail.sohu.com'
        self.driver.maximize_window()
        self.driver.get(url)
        time.sleep(5)
        try:
            # userName = self.driver.find_element_by_xpath("//*[@id='theme']/form/div[1]/div[1]/input")
            userName = self.driver.find_element_by_xpath("//input[@placeholder='请输入您的邮箱']")
            userName.clear()
            userName.send_keys('Ruzi_li@sohu.com')
            # pwd = self.driver.find_element_by_xpath("//*[@id='theme']/form/div[2]/div[1]/input")
            pwd = self.driver.find_element_by_xpath("//input[@placeholder='请输入您的密码']")
            pwd.clear()
            pwd.send_keys('nzz372135094')
            login = self.driver.find_element_by_xpath("//input[@value='登 录']")
            login.click()
            wait = WebDriverWait(self.driver,10)
            wait.until(EC.element_to_be_clickable((By.XPATH,"//li[text()='写邮件']")))
            self.driver.find_element_by_xpath("//li[text()='写邮件']").click()
            time.sleep(5)
            receiver = self.driver.find_element_by_xpath("//div[@arr='mail.to_render']//input")
            receiver.send_keys('liqinjia@arkgrace.com;')
            time.sleep(5)
            # subject = self.driver.find_element_by_xpath("//input[@ng-model='mail.subject']")
            subject = self.driver.find_element_by_xpath(".//*[@id='mailContent']/div/div[1]/div[1]/div[4]/input")
            subject.send_keys('这是一封测试邮件！')
            time.sleep(5)
            iframe = self.driver.find_element_by_xpath("//iframe[contains(@id,'ueditor_0')]")
            self.driver.switch_to.frame(iframe)
            editBox = self.driver.find_element_by_xpath("/html/body")
            editBox.send_keys('邮件的正文内容')
            self.driver.switch_to.default_content()
            time.sleep(5)
            #self.driver.find_element_by_xpath("//sapn[.='发送']").click()
            self.driver.find_element_by_xpath(".//*[@id='mailContent']/div/div[2]/span[1]").click()
            wait.until(EC.visibility_of_element_located((By.XPATH,'//span[.="发送成功"]')))
            print('邮件发送成功')
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