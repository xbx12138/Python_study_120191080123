#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:03_twoList_same_output.py
# author:Asus
# datetime:2021/3/31 21:06
# software: PyCharm
'''
3  编写一个函数, 传入一个数字列表, 输出列表中的奇数;
   数字列表请用随机数函数生成;
'''
# import module your need

import random


def Numb(list_Num):
    print('奇数有：')
    for i in list_Num:
        if i % 2 == 1:
            print(i,end=' ')


if __name__ == '__main__':
    list_Num = [random.randint(0, 100) for i in range(10)]
    print(list_Num)
    Numb(list_Num)