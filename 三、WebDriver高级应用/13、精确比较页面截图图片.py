# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 14:50
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : 13、精确比较页面截图图片.py
# @Software: PyCharm

from selenium import webdriver
import unittest
import time
from PIL import Image

class ImageCompare(object):

    def make_regalur_image(self,img,size=(256,256)):
        return img.resize(size).convert('RGB')

    def split_image(self,img,part_size=(64,64)):
        w,h=img.size
        pw,ph=part_size
        assert w%pw==h%ph==0
        return [img.crop((i,j,i+pw,j+ph)).copy() for i in range(0,w,pw) for j in range(0,h,ph)]

    def hist_similar(self,lh,rh):
        assert len(lh) == len(rh)
        return sum(1-(0 if l == r else float(abs(l-r))/max(l,r)) for l,r in zip(lh,rh))/len(lh)

    def calc_similar(self,li,ri):
        return sum(self.hist_similar(l.histogram(),r.histogram()) for l,r in zip(self.split_image(li),self.split_image(ri)))/16.0

    def calc_similar_by_path(self,lf,rf):
        li,ri = self.make_regalur_image(Image.open(lf)),self.make_regalur_image(Image.open(rf))
        return self.calc_similar(li,ri)

class TestDemo(unittest.TestCase):
    def setUp(self):
        self.IC = ImageCompare()
        self.driver = webdriver.Chrome()

    def test_ImageComparison(self):
        url = 'http://www.sogou.com'
        self.driver.maximize_window()

        self.driver.get(url)
        time.sleep(3)
        self.driver.save_screenshot("F:\\ScreenPicture\\sogou1.png")

        self.driver.get(url)
        time.sleep(3)
        self.driver.save_screenshot("F:\\ScreenPicture\\sogou2.png")

        print(self.IC.calc_similar_by_path("F:\\ScreenPicture\\sogou1.png","F:\\ScreenPicture\\sogou2.png")*100)

    def tearDown(self):
        self.driver.quit()


if __name__ == '__main__':
    unittest.main()