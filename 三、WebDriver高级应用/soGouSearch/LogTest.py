# -*- coding: utf-8 -*-
# @Time    : 2018/4/17 18:33
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : LogTest.py
# @Software: PyCharm

import logging.config

logging.config.fileConfig("Logger.conf")


def debug(message):
    logging.debug(message)


def warning(message):
    logging.warning(message)


def info(message):
    logging.info(message)


