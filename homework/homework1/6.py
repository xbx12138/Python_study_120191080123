#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:6.py
# author:Asus
# datetime:2021/3/4 20:19
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 6  前面2个元素为0，1，输出100以内的斐波那契数列；


if __name__ == "__main__":
    num = [0]
    n = 1
    while (n < 100):
        num.append(n)
        n = num[-2] + num[-1]
    print(num)
