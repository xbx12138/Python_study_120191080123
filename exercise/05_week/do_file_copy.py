#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_file_copy.py
# author:Asus
# datetime:2021/4/1 21:13
# software: PyCharm
'''
练习:
     将一个文件夹下的某个文件,拷贝到另外一个文件夹下去;
     提示:    写一个copy函数，接受两个参数，第一个参数是源文件的位置，第二个#参数是目标位置，将源文件copy到目标位置。
                还需要判断一下这个文件之前是否存在;  读源文件的内容; 创建目标文件; 读到的内容,再写入到目标文件
'''
# import module your need
import os

def copy(path_goal, path_Source):
    if os.path.isfile(path_Source):
        with open(path_Source, 'r', encoding='utf-8') as fr:
            date = fr.read()
            print(date)
        with open(path_goal, 'w', encoding='utf-8') as fw:
            fw.write(date)


if __name__ == '__main__':
    copy('./copy/goal/test.txt', './copy/source/copy.txt')
