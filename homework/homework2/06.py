#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:06.py
# author:Asus
# datetime:2021/4/1 22:52
# software: PyCharm
'''
6  定义一个函数, 打印输出n以内的斐波那契数列;
'''


# import module your need

def fibonacci(n):
    num = [0, 1]
    for i in range(n - 2):
        num.append(num[-2] + num[-1])
    for i in num:
        print(i, end=' ')


if __name__ == '__main__':
    fibonacci(5)
