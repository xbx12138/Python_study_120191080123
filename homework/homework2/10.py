#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:10.py
# author:Asus
# datetime:2021/4/4 11:56
# software: PyCharm
'''
10 编写一个函数caculate, 可以实现2个数的运算(加,减 乘,除)
'''


# import module your need

def caculate(a, c, b):
    if c == '+':
        return a + b
    elif c == '-':
        return a - b
    elif c == '*':
        return a * b
    elif c == '/':
        while b == 0:
            b = input('除数不能为0,请重新输入：')
        return a / b


if __name__ == '__main__':
    a = int(input('输入第一个数：'))
    c = input('输入运算符(+,-,*,/):')
    b = int(input('输入第二个数:'))
    print(f'{a}{c}{b}={caculate(a,c,b)}')
