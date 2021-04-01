#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_os.py
# author:Asus
# datetime:2021/4/1 21:07
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os

# os.mkdir(r'C:\ATA\123')
# os.remove(r'C:\ATA\123\dad123.txt')
# list = os.listdir(r'C:\ATA\123')
# for i in list:
#     path=os.path.join(r'C:\ATA\123', i)
#     if os.path.isfile(path):
#         print(path)
#         os.remove(path)
#     elif os.path.isdir(path):
#         print(path)
#         os.removedirs(path)

def list_dir(lpath):
    list1=os.listdir(lpath)
    for i in list1:
        path=os.path.join(lpath,i)
        if os.path.isfile(path):
            print(path)
        elif os.path.isdir(path):
            list_dir(path)

if __name__=='__main__':
    list_dir(r'C:\ATA\123')