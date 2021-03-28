#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_import.py
# author:Asus
# datetime:2021/3/28 10:07
# software: PyCharm
'''
1.3 需要导入的模块在父文件夹中--请做课堂练习
'''
# import module your need

import sys

sys.path.append(r'D:\pythonProject\Python_study_120191080123\exercise\01_week')

import Helloworld

if __name__=='__main__':
    Helloworld.main()