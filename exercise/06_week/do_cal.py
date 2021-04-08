#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_cal.py
# author:Asus
# datetime:2021/4/8 15:01
# software: PyCharm
'''

'''


# import module your need

def add(x, y):
    return x + y


def minus(x, y):
    return x - y


def mul(x, y):
    return x * y


def div(x, y):
    while y == 0:
        y = input('除数不能为0, 请重新输入：')
    return x / y;


def cal(x,y,func):
    return func(x,y)


if __name__=='__main__':
    print(cal(1,2,add))

