# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 16:12
# @Author  : 'Robin Li
# @Email   : liqinjia372135@163.com
# @File    : FileUtil.py
# @Software: PyCharm

from DateUtil import currentDate,currentTime
import os



def createDir():
    currentPath = os.path.dirname(os.path.abspath(__file__))
    today = currentDate()
    dateDir = os.path.join(currentPath,today)
    print(dateDir)
    if not os.path.exists(dateDir):
        os.mkdir(dateDir)
    now = currentTime()
    timeDir = os.path.join(dateDir,now)
    print(timeDir)

    if not os.path.exists(timeDir):
        os.mkdir(timeDir)
    return timeDir