#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_tup.py
# author:Asus
# datetime:2021/3/8 15:52
# software: PyCharm
'''
练习:
     定义元组,进行基本的操作(元组的基本运算,元素的输出,内置函数的使用); 定义一个元组,来保存成绩,输出最高分;
'''
# import module your need

import random

tup1 = (1, 2, 3)
tup2 = (4, 5, 6)
print(tup1[0:2])  # 切片
print(len(tup1))  # 计算元素个数
tup3 = tup1 + tup2  # 连接
print(tup3)
print(('Hi', 'o') * 4)  # 复制
print(6 in tup3)  # 元素是否存在

list1 = [random.randint(1, 100) for _ in range(10)]

tup4 = tuple(list1)
for x in tup4: print(x, end=' ')  # 迭代
print(f'\n最大值：{max(tup4)}最小值：{min(tup4)}')
