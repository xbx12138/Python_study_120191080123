#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:5.py
# author:Asus
# datetime:2021/3/4 19:46
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 5  使用random模块，生成随机数，来初始化一个列表，元组；
# 使用了 random 模块的 randint() 函数来生成随机数，查询一下相关函数的用法；

import random

if __name__ == "__main__":
    print('初始化列表...')
    list1 = []
    for i in range(random.randint(1, 10)):
        list1.append(random.randint(1, 100))
    print(list1)
    print('初始化元组...')
    tup1 = ()
    for i in range(random.randint(1, 10)):
        tup2 = (random.randint(1, 100),)
        tup1 = tup1 + tup2
    print(tup1)
