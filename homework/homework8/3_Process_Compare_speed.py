#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3.py
# author:Asus
# datetime:2021/5/17 20:51
# software: PyCharm
'''
3  多进程练习：
计算1～100000之间所有素数的个数， 要求如下:
- 编写函数判断一个数字是否为素数，然后统计素数的个数；
-对比1: 对比使用多进程和不使用多进程两种方法的统计速度。
-对比2：对比开启4个多进程和开启10个多进程两种方法的速度。

'''
# import module your need
import ntpath
from math import sqrt
from multiprocessing import Pool
from multiprocessing import Manager
import time, os, functools


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


def isPrime(num):
    start = 2
    end = int(sqrt(num))
    for i in range(start, end + 1):
        if num % i == 0:
            return False
    return True


@timmer
def no_mp():
    count = 0
    for i in range(2, 100000):
        if isPrime(i):
            count += 1
    return count


def fun1(flag, q):
    count = 0
    for i in range(flag * 25000, flag * 25000 + 25000):
        if isPrime(i) and i != 0 and i != 1:
            count += 1
    q.put(count)


@timmer
def do_mp():
    count = 0
    po = Pool(4)
    q = Manager().Queue()
    for i in range(0, 4):
        po.starmap(fun1, [(i, q)])
    po.close()
    po.join()
    for i in range(q.qsize()):
        count += q.get(True)
    return count


def fun2(flag, q):
    count = 0
    for i in range(flag * 10000, flag * 10000 + 10000):
        if isPrime(i) and i != 0 and i != 1:
            count += 1
    q.put(count)


@timmer
def do_10_mp():
    count = 0
    po=Pool(10)
    q=Manager().Queue()
    for i in range(0,10):
        po.starmap(fun2,[(i,q)])
    po.close()
    po.join()
    for i in range(q.qsize()):
        count += q.get(True)
    return count


if __name__ == '__main__':
    print(no_mp())
    print(do_mp())
    print(do_10_mp())
