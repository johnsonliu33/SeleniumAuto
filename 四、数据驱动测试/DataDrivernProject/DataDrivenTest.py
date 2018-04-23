# -*- coding: utf-8 -*-
# @Time    : 2018/4/19 19:55
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : DataDrivenTest.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time,logging,ddt
from selenium.common.exceptions import NoSuchElementException
import traceback
from ReportTemolate import htmlTemplate

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt= '%a,%d %b %Y %H：%M：%S',
    filename='F:\\DataDriverTesting\\report2.log',
    filemode='w'
)

@ddt.ddt
class TestDemo(unittest.TestCase):
    @classmethod
    def setUpClass(cls):
        TestDemo.trStr = ''

    def setUp(self):
        self.driver = webdriver.Chrome()
        status = None
        flag = 0

    @ddt.file_data('test_data_list.json')
    def test_dataDrivenByFile(self,value):
        flagDict={0:'red',1:'#00AC4E'}

        url = 'http://www.baidu.com'
        self.driver.get(url)
        self.driver.maximize_window()
        print(value)
        testdata,expectdata = tuple(value.strip().split('||'))
        self.driver.implicitly_wait(10)

        try:
            start = time.time()
            startTime = time.strftime('%Y-%m-%d %H:%M:%S',time.localtime())
            self.driver.find_element_by_id('kw').send_keys(testdata)
            self.driver.find_element_by_id('su').click()
            time.sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error('查找的页面元素不存在，异常堆栈信息：'+str(traceback.print_exc()))
            status = 'fail'
            flag = 0
        except AssertionError as e:
            logging.info('搜索:%s,期望:%s,失败'%(testdata,expectdata))
            status = 'fail'
            flag =0
        except Exception as e:
            logging.error('未知错误，错误信息：'+str(traceback.format_exc()))
            status = 'fail'
            flag =0
        else:
            logging.info('搜索:%s，期望 :%s,通过'%(testdata,expectdata))
            status = 'pass'
            flag =1

        wasteTime = time.time() - start -3
        TestDemo.trStr +='''
        <tr>
            <td>%s</td>
            <td>%s</td>
            <td>%s</td>
            <td>%.2f</td>
            <td style='color:%s'>%s</td>
        </tr>'''%(testdata,expectdata,startTime,wasteTime,flagDict[flag],status)


    def tearDown(self):
        self.driver.quit()

    @classmethod
    def tearDownClass(cls):
        htmlTemplate(TestDemo.trStr)

if __name__ == '__main__':
    unittest.main()