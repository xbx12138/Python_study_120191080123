#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_list2.py
# author:Asus
# datetime:2021/3/8 15:01
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

import random

score = [random.randint(60, 100) for _ in range(10)]

Max1 = max(score);
Min1 = min(score);
Sum = sum(score)

avg = Sum / len(score)
print(f'{score}\n最高分：{Max1}\n最低分：{Min1}\n总分：{Sum}\n平均分：{avg}')
