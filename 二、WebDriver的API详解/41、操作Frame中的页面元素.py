__author = 'Robin'

from selenium import webdriver
import unittest
from selenium.webdriver.support import expected_conditions as EC
from selenium.webdriver.support.ui import WebDriverWait
from selenium.common.exceptions import TimeoutException


class VisitSogouByChrome(unittest.TestCase):
    def setUp(self):
        self.driver = webdriver.Chrome()

    def test_handleFrame(self):
        url = 'F:\\HTMLTest\\41\\frameset.html'
        self.driver.get(url)
        self.driver.switch_to.frame(0)
        leftFrameText = self.driver.find_element_by_xpath('//p')
        self.assertAlmostEqual(leftFrameText.text,'这是左侧 frame 页面上的文字')
        self.driver.find_element_by_tag_name('input').click()
        try:
            alertWindow = WebDriverWait(self.driver,10,0.2).until(EC.alert_is_present())
            print(alertWindow.text)
            alertWindow.accept()
        except TimeoutException as e:
            print(e)

        self.driver.switch_to.default_content()
        self.driver.switch_to.frame(self.driver.find_elements_by_tag_name('frame')[1])
        assert '这是中间 frame 页面上的文字'in self.driver.page_source
        self.driver.find_element_by_tag_name('input').send_keys('我在中间 frame')
        self.driver.switch_to.default_content()

        self.driver.switch_to.frame(self.driver.find_element_by_id('rightframe'))
        assert '这是右侧 frame 页面上的文字'in self.driver.page_source
        self.driver.switch_to.default_content()

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()