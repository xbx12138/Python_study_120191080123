#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_file.py
# author:Asus
# datetime:2021/3/28 10:58
# software: PyCharm
'''
练习:
   构造上述文件结构,分别在指定位置打开文件进行写入操作(
   同级文件夹里面打开;
   同级目录下的子目录里面打开;
   上一级文件目录中的其他文件夹中打开);
'''
# import module your need

import os

with open(r'file_text', 'r', encoding='utf-8') as f1:
    print(f1.read())
with open(r'do_os_path\file_text.txt','r',encoding='utf-8') as f2:
    print(f2.read())
with open(r'..\01_week\file_text.txt','r',encoding='utf-8') as f3:
    print(f3.read())
