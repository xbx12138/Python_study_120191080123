#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2.py
# author:Asus
# datetime:2021/5/17 20:06
# software: PyCharm
'''
2 给定一组数据网址数据，请判断这些网址是否可以访问； 用多线程的方式来实现；
   请查资料，Python的 requests库，如何判断一个网址可以访问；
提示 ：使用requests模块
   def getHtmlText(url):
    try:        # 网络连接有风险，异常处理很重要
        r = requests.get(url,timeout=30)    # 查一下这个方法的使用
        r.raise_for_status()       # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
         return "产生异常"
  数据文件（1000个网址）：
'''
# import module your need

import requests
from concurrent.futures import ThreadPoolExecutor


def getHtmlText(url):
    try:  # 网络连接有风险，异常处理很重要
        r = requests.get(url, timeout=30)  # 查一下这个方法的使用
        r.raise_for_status()  # 如果状态不是200，引发HTTPError异常
        r.encoding = r.apparent_encoding
        return r.text
    except:
        return "产生异常"


def geturl():
    with open('2/url_data.txt', 'r') as fr:
        urls = fr.read().split('\n')
        return urls


def fun(urls, i):
        if len(getHtmlText(urls[i])) == 4:
            print(f'{urls[i]} 不可访问')
        else:
            print(f'{urls[i]} 可正常访问')


def ThreadPool():
    with ThreadPoolExecutor(max_workers=1000) as t:
        urls = geturl()
        all_task = [t.submit(fun(urls, index), index) for index in range(0, 1000)]


if __name__ == '__main__':
    ThreadPool()
