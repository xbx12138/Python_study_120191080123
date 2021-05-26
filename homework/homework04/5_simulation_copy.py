#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:5.py
# author:Asus
# datetime:2021/4/24 9:49
# software: PyCharm
'''
5  通过Python来模拟实现一个txt文件的拷贝过程;
'''
# import module your need

import os

if __name__ == '__main__':
    file_path = input('请输入要复制的文件路径')
    path_idx = file_path.rfind('/')
    file_path_1 = file_path[:path_idx + 1]
    file_name = file_path[path_idx + 1:]
    idx = file_name.rfind('.')
    file_name_1 = file_name[:idx]
    file_name_2 = file_name[idx:]
    new_file_name = ''
    if os.path.exists(file_path_1 + file_name_1 + " - 副本" + file_name_2) == False:
        new_file_name = file_path_1 + file_name_1 + " - 副本" + file_name_2
    else:
        for i in range(2, 100):
            if os.path.exists(file_path_1 + file_name_1 + " - 副本(" + str(i) + ")" + file_name_2) == False:
                new_file_name = file_path_1 + file_name_1 + " - 副本(" + str(i) + ")" + file_name_2
                break
            else:
                i += 1
                continue
    with open(file_path, 'rb') as fr:
        with open(new_file_name, 'wb') as fw:
            while True:
                info = fr.read(1024)
                if not info:
                    break
                fw.write(info)
