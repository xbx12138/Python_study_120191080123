#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:03.py
# author:Asus
# datetime:2021/3/4 18:27
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 3 定义2个列表，并初始化；  找出这2个列表中，相同的元素并输出；

if __name__ == "__main__":
    list1 = [2000, 5, 65, '男', 'xbx', 165, 12]
    list2 = [65, 'xbx', 12, 65, '女', 5]
    for obj in list1:
        if list2.count(obj) != 0:
            print(obj)
