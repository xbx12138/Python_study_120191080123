#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:1.py
# author:Asus
# datetime:2021/5/17 19:43
# software: PyCharm
'''
1  有100个同学的分数：数据请用随机函数生成；
     A  利用多线程程序（比如，5个线程，每个线程负责输出20条记录），快速输出这100个同学的信息；
     B 利用线程池来实现；
'''
# import module your need

from concurrent.futures import ThreadPoolExecutor
import random


def fun(page):
    id = random.sample(range(1, 21), 20)
    for i in range(0, 20):
        print(f'学号：{id[i] + page * 20}    成绩：{random.randint(60, 100)}')


def ThreadPool():
    with ThreadPoolExecutor(max_workers=5) as t:
        all_task = [t.submit(fun(page), page) for page in range(0, 5)]


if __name__ == '__main__':
    ThreadPool()
