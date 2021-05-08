#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:4.py
# author:Asus
# datetime:2021/5/8 16:47
# software: PyCharm
'''
4  编写装饰器来实现，对目标函数进行装饰,计算函数的运行耗时，
    分3种情况：目标函数无参数无返回值，目标函数有参数，目标函数有返回值；
     三个目标函数分别为：
     A 打印输出20000之内的素数；
     B 计算整数2-10000之间的素数的个数；
     C 计算整数2-M之间的素数的个数；
'''
# import module your need

import time
import functools
from math import sqrt


def timmer(func):
    @functools.wraps(func)
    def wrapper(*args, **kwargs):
        print('call %s():' % func.__name__)
        start_time = time.time()
        res = func(*args, **kwargs)
        end_time = time.time()
        print("运行时间为%s" % (end_time - start_time))
        return res

    return wrapper


def isprime(num):
    start = 2
    end = int(sqrt(num))
    for i in range(start, end + 1):
        if num % i == 0:
            return False
    return True


@timmer
def A():
    for i in range(2, 20000):
        if isprime(i):
            print(i, end=' ')


@timmer
def B():
    count = 0
    for i in range(2, 10000):
        if isprime(i):
            count += 1
    return count


@timmer
def C(M):
    count = 0
    for i in range(2, M):
        if isprime(i):
            count += 1
    return count


if __name__ == '__main__':
    M = 5000
    A()
    print(f'2~10000的素数共有{B()}个')
    print(f'2~{M}的素数共有{C(M)}个')
