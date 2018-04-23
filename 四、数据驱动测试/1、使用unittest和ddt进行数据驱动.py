# @Time    : 2018/4/19 19:22
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : 1、使用unittest和ddt进行数据驱动.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time,logging,ddt
from selenium.common.exceptions import NoSuchElementException
import traceback

logging.basicConfig(
    level=logging.INFO,
    format='%(asctime)s %(filename)s[line:%(lineno)d] %(levelname)s %(message)s',
    datefmt= '%a,%d %b %Y %H：%M：%S',
    filename='F:\\DataDriverTesting\\report.log',
    filemode='w'
)

@ddt.ddt
class TestDemo(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    @ddt.data(['神奇动物在哪里','叶茨'],
              ['疯狂动物城','古德温'],
              ['大话西游之月光宝盒','周星驰'])

    @ddt.unpack
    def test_dataDriverByObj(self,testdata,expectdata):
        url = 'http://www.baidu.com'
        self.driver.get(url)
        self.driver.implicitly_wait(10)
        try:
            self.driver.find_element_by_id('kw').send_keys(testdata)
            self.driver.find_element_by_id('su').click()
            time.sleep(3)
            self.assertTrue(expectdata in self.driver.page_source)
        except NoSuchElementException as e:
            logging.error('查找的页面元素不存在，异常堆栈信息：'+str(traceback.print_exc()))
        except AssertionError as e:
            logging.info('搜索:%s,期望:%s,失败'%(testdata,expectdata))
        except Exception as e:
            logging.error('未知错误，错误信息：'+str(traceback.format_exc()))
        else:
            logging.info('搜索:%s，期望 :%s,通过'%(testdata,expectdata))

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()