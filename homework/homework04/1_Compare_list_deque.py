#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:1.py
# author:Asus
# datetime:2021/4/18 23:33
# software: PyCharm
'''
1 定义一个10个元素的列表，通过列表自带的函数，实现元素在尾部插入和头部插入并记录程序运行的时间；
用deque来实现，同样记录程序所耗费的时间；输出这2个时间的差值；
    提示：列表原生的函数实现头部插入数据：list.insert(0, v)；list.append（2）)
'''
# import module your need

from collections import deque
import time
from timeit import default_timer as timer


def fun1(list, v):
    tic = timer()
    # time1 = time.time()
    list.insert(0, v)
    list.append(v)
    # time2 = time.time()
    toc = timer()
    print(list)
    return toc - tic  # time2 - time1


def fun2(list, v):
    tic = timer()
    # time1 = time.time()
    list.append(v)
    list.appendleft(v)
    # time2 = time.time()
    toc = timer()
    print(list)
    return toc - tic  # time2 - time1


if __name__ == '__main__':
    list = ['1', '2', '3', '4', '5', '6', '7', '8', '9', '0']
    q = deque(['1', '2', '3', '4', '5', '6', '7', '8', '9', '0'])
    time1 = fun1(list, 'x')
    time2 = fun2(q, 'x')
    if time1 > time2:
        time = time1 - time2
    else:
        time = time2 - time1
    print(f'list花费时间： {time1} ;deque花费时间： {time2} ;两者差值：{time}')
