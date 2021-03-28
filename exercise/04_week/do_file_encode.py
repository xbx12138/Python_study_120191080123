#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_file_encode.py
# author:Asus
# datetime:2021/3/28 11:29
# software: PyCharm
'''
练习:  读取文件里面的内容(包含中文), 进行打印输出显示;
         注意:  请设置文件的不同编码格式进行观察;  另外,文件内容中包含中文字符;
'''
# import module your need

import os

with open('file_text','r',encoding='utf-8') as f:
    print(f.read())