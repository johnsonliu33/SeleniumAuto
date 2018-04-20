__author = 'Robin'

from selenium import webdriver
import unittest


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_handleIFrame(self):
        url = 'F:\\HTMLTest\\43\\frameset.html'
        self.driver.get(url)
        self.driver.switch_to.frame(0)
        assert '这是左侧 frame 页面上的文字' in self.driver.page_source

        self.driver.switch_to.frame(self.driver.find_element_by_id('showIframe'))
        assert '这是 iframe 页面上的文字'in self.driver.page_source

        self.driver.switch_to.default_content()
        assert 'frameset 页面'==self.driver.title

        self.driver.switch_to.frame(1)
        assert '这是中间 frame 页面上的文字' in self.driver.page_source


    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()