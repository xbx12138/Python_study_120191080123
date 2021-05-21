#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:09.py
# author:Asus
# datetime:2021/4/4 11:45
# software: PyCharm
'''
9  定义一个函数，函数接收一个数组，并把数组里面的数据从小到大排序(冒泡排序,  也可以直接使用相关的函数);
'''
# import module your need

import random


def sort(numbers):
    numbers.sort()
    return numbers


if __name__ == '__main__':
    numbers = [random.randint(10, 100) for i in range(10)]
    print(numbers)
    print(sort(numbers))
