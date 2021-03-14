#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_dict_adddel.py
# author:Asus
# datetime:2021/3/14 13:37
# software: PyCharm
'''
练习:
    字典的元素的增加, 修改,删除; 并观察输出
'''
# import module your need
dict1 = {'ID': 12001, 'name': 'Tom', 'class': '软件1901', 'age': '18'}
print(f'修改前：{dict1}')

dict1['weight']=60#add
print(f'增：{dict1}')
dict1['age']=20#update
print(f'改：{dict1}')
del dict1['weight']#del
print(f'删：{dict1}')

