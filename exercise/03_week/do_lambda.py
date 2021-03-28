#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_lambda.py
# author:Asus
# datetime:2021/3/15 14:45
# software: PyCharm
'''
练习:
       初始化一个列表(1-20之间的整数) ; 然后 使用匿名函数,列表解析式, 来打印输出一个列表中的奇数;
'''
# import module your need

import random

list1 = [random.randint(1, 20) for _ in range(10)]
fun = lambda x: x % 2 == 1
print(list(filter(fun, list1)))
