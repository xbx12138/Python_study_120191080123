#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:4.py
# author:Asus
# datetime:2021/4/5 1:12
# software: PyCharm
'''
4 题目要求：
 在当前目录新建目录img, 里面包含10个文件, 10个文件名各不相同(X4G5.png)
 将当前img目录所有以.png结尾的后缀名改为.jpg.
'''
# import module your need

import os

if __name__ == '__main__':
    file_list = os.path.join(os.getcwd(), 'img')
    for i in os.listdir(file_list):
        currentdir = os.path.join(file_list, i)
        fname = os.path.splitext(i)[0]
        newname = os.path.join(file_list, fname + '.jpg')
        os.rename(currentdir, newname)
