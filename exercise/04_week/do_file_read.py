#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_file_read.py
# author:Asus
# datetime:2021/3/28 11:41
# software: PyCharm
'''
练习:   一个文件内容的如下,请读取文件的内容, 并输出;
            姓名      学号      分数
            张三      101         78
            李四      102         87
            王五       103        83
'''
# import module your need

f=open('file_sort.txt','r',encoding='utf-8')
for line in f.readline():
    print(line.strip())