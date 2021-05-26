#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:02_dict_stu_score_output_80.py
# author:Asus
# datetime:2021/3/4 17:11
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 2 一个字典中，存放了10个学生的学号（key）和分数（value）；请筛选输出，大于80分的同学（按照格式：学号：分数）；

if __name__ == "__main__":
    dict1 = {'001': 99, '002': 65, '003': 77, '004': 85, '005': 88,
             '006': 79, '007': 83, '008': 90, '009': 74, '010': 80}

    for k, v in dict1.items():
        if v > 80:
            print('学号：', k, '分数：', v)
