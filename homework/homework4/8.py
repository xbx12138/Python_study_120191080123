#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:8.py
# author:Asus
# datetime:2021/4/24 10:53
# software: PyCharm
'''
8 京东二面笔试题
1） 生成一个大文件ip.txt,要求1200行，每行随机为172.25.254.1---172.25.254.254之间的一个ip地址;
2） 读取ip.txt文件统计这个文件中ip出现频率排前10的ip
'''
# import module your need

import random
import os


def init():
    with open('./8/ip.txt', 'a', encoding='utf-8') as fa:
        for i in range(0, 1200):
            info = str(random.randint(1, 255))
            ip = '172.25.254.' + info + '\n'
            fa.write(ip)


def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i][1] < lists[j][1]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


def count():
    with open('./8/ip.txt', 'r', encoding='utf-8') as fr:
        ips = fr.read()
        list_ip = ips.split('\n')
    ips_ = {}
    ip_list = []
    for ip in list_ip:
        if ip in ips_:
            ips_[ip] += 1
        else:
            ips_[ip] = 1
    for k, v in ips_.items():
        tup = (k, v)
        ip_list.append(tup)

    bubble_sort(ip_list)
    for i in range(1, 11):
        print(f'{i}: {ip_list[i][0]} 次数：{ip_list[i][1]}')


if __name__ == '__main__':
    init()
    count()
