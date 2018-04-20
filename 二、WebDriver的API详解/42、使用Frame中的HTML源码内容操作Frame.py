__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_handleFrameByPageSource(self):
        url = 'F:\\HTMLTest\\41\\frameset.html'
        self.driver.get(url)
        frameList = self.driver.find_elements_by_tag_name('frame')
        for frame in frameList:
            self.driver.switch_to.frame(frame)
            if '中间 frame' in self.driver.page_source:
                p = self.driver.find_element_by_xpath('//p')
                self.assertAlmostEqual('这是中间 frame 页面上的文字',p.text)
                self.driver.switch_to.default_content()
                break
            else:
                self.driver.switch_to.default_content()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()