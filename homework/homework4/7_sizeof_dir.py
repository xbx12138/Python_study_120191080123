#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:7.py
# author:Asus
# datetime:2021/4/24 10:45
# software: PyCharm
'''
7 使用python代码统计一个文件夹中所有文件的总大小
'''
# import module your need

import os

def size(lpath):
    list1 = os.listdir(lpath)
    file_size=0
    for i in list1:
        path = os.path.join(lpath, i)
        if os.path.isfile(path):
            file_size += os.stat(path).st_size
        elif os.path.isdir(path):
            file_size +=size(path)
    return file_size

if __name__ == '__main__':
    path=input('请输入路径:')
    print(f'该文件夹总大小为{size(path)/1000}KB')