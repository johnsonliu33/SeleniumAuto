# -*- coding: utf-8 -*-
# @Time    : 2018/4/23 18:29
# @Author  : Robin Li
# @Email   : liqinjia372135@163.com
# @File    : steps.py
# @Software: PyCharm

from lettuce import *


def factorial(number):
    number = int(number)
    if (number == 0) or (number == 1):
        return 1
    else:
        return reduce(lambda x, y: x*y, range(1, number + 1))


@step('I have the number(\d + )')
def have_the_number(step, number):
    world.number = int(number)


@step('I compute its factorial')
def compute_its_factorial(step):
    world.number = factorial(world.number)


@step('I see the number(\d + )')
def check_number(step, expected):
    expected = int(expected)
    assert world.number == expected, 'Got %d' % world.number