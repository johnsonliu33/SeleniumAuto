__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_cookies(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        cookies = self.driver.get_cookies()
        for cookie in cookies:
            print('%s -> %s -> %s -> %s -> %s'%(cookie['domain'],cookie['name'],cookie['value'],cookie['expiry'],cookie['path']))
        ck = self.driver.get_cookie('SUV')
        print('%s -> %s -> %s -> %s -> %s'%(ck['domain'],ck['name'],ck['value'],ck['expiry'],ck['path']))

        print(self.driver.delete_cookie('ABTEST'))
        self.driver.delete_all_cookies()
        cookies = self.driver.get_cookies()
        print(cookies)

        self.driver.add_cookie({'name':'gloryroadTrain','value':'1478393043423'})
        cookie = self.driver.get_cookie('gloryroadTrain')
        print(cookie)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()