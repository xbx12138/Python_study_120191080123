#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:1.py
# author:Asus
# datetime:2021/4/24 12:09
# software: PyCharm
'''
1  编写一个装饰器，能计算其他函数的运行时间；
'''
# import module your need

import time
import random


def outer(func):
    def inner():
        start_time = time.time()
        func()
        end_time = time.time()
        print("运行时间为%s" % (end_time - start_time))
    return inner


@outer
def test():
    time.sleep(random.randrange(1, 5))
    print('123')


if __name__ == '__main__':
    test()
