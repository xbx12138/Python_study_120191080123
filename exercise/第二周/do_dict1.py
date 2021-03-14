#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_dict1.py
# author:Asus
# datetime:2021/3/11 16:03
# software: PyCharm
'''
练习:
    定义一个字典,存放某个同学的信息(学号,姓名,班级,年龄);   再定义另外一个字典,存放5个同学的学号,姓名信息;
    通过键来访问相应的数据; 或者整体输出
'''
# import module your need

dict1 = {'ID': 12001, 'name': 'Tom', 'class': '软件1901', 'age': '18'}
print(dict1)

dict_stu = {12011: 'tx1', 12012: 'tx2', 12013: 'tx3', 12014: 'tx4', 12015: 'tx5'}
i=12013
print(f'学号：{i}，姓名： {dict_stu[12013]}')
