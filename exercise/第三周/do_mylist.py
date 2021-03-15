#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_mylist.py
# author:Asus
# datetime:2021/3/15 14:20
# software: PyCharm
'''
练习:
     定义一个函数,  打印输出列表里面的元素;  然后增加列表中的元素, 然后再输出新的列表;  主程序中,打印这个列表的地址(传参之前,传参之后);
'''
# import module your need

import random


def printf(l):
    for i in l:
        print(i,end=',')
    l.append(random.randint(1, 10));
    print()
    for i in l:
        print(i,end=',')
    print()


if __name__ == "__main__":
    l = []
    for i in range(1, 10):
        l.append(random.randint(1, 10))
    print(id(l))
    printf(l)
    print(id(l))
