# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 16:12
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : DateUtil.py
# @Software: PyCharm

from datetime import datetime
import time

def currentDate():
    date = time.localtime()
    today = str(date.tm_year) + '-' + str(date.tm_mon) + '-' + str(date.tm_mday)
    return today

def currentTime():
    timeStr = datetime.now()
    now = timeStr.strftime('%H-%M-%S')
    return now

if __name__ =='__main__':
    print(currentDate())
    print(currentTime())