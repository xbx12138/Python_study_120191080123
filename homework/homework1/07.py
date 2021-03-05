#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:07.py
# author:Asus
# datetime:2021/3/4 20:32
# software: PyCharm
'''
this is functiondescription
'''


# import module your need

# 7 打印输出9*9乘法表

def getInfo(x, y):
    # print(x, 'x', y, '=', x * y, end="  ")
    print(x, end="x")
    print(y, end="=")
    print(x * y, end=" ")


if __name__ == "__main__":
    for i in range(1, 10):
        for j in range(1, i + 1):
            getInfo(i, j)
        print()
