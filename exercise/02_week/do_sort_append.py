#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_sort_append.py
# author:Asus
# datetime:2021/3/8 15:13
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import random

score=[random.randint(60,100) for _ in range(5)]

print(score)
score.sort()
print(score)
score.append(random.randint(60,100))
print(score)