#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:6.py
# author:Asus
# datetime:2021/4/24 10:19
# software: PyCharm
'''
6  通过Python来实现显示给定文件夹下的所有文件和文件夹,以及时间，如果是文件，显示大小; 输出格式效果如下:
    名称         日期                   类型（文件夹或者 文件）       大小
'''
# import module your need

import os
import datetime

def list_dir(lpath):
    list1 = os.listdir(lpath)
    print('名称          修改日期                类型          大小')
    for i in list1:
        path = os.path.join(lpath, i)
        path_idx = path.rfind('\\')
        file_path_1 = path[:path_idx + 1]
        file_name = path[path_idx + 1:]
        date = datetime.datetime.fromtimestamp(os.path.getmtime(path))
        update_time = date.strftime('%Y/%m/%d %H:%M')


        if os.path.isfile(path):
            path_type='文本文档'
            file_size=os.stat(path).st_size
            print(f'{file_name}      {update_time}         {path_type}       {file_size/1000}kb')
        elif os.path.isdir(path):
            path_type='文件夹'
            print(f'{file_name}      {update_time}         {path_type}  ')


if __name__ == '__main__':
    path = input("请输入文件夹路径:")
    list_dir(path)
