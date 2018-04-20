__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_captureScreenInCurrentWindow(self):
        url = 'http://www.sogou.com'
        self.driver.get(url)
        try:
            result = self.driver.get_screenshot_as_file('F:\\ScreenPicture\\pic01.png')
            print(result)
        except IOError as e:
            print(e)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()