#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:07.py
# author:Asus
# datetime:2021/4/1 23:21
# software: PyCharm
'''
7  随机生成20个学生的成绩; 判断这20个学生成绩的等级; 用函数来实现;
    A---成绩>=90;
    B-->成绩在 [80,90)
    C-->成绩在 [70,80)
    D-->成绩<70
'''

# import module your need

import random


def rank(score):
    A = {}
    B = {}
    C = {}
    D = {}

    for k, v in score.items():
        if v >= 90:
            A[k] = v
        elif 80 <= v < 90:
            B[k] = v
        elif 70 <= v < 80:
            C[k] = v
        elif v < 70:
            D[k] = v
    print('成绩为A的同学有：')
    for k, v in A.items():
        print(f'{k}：{v}', end=' ;')
    print('\n成绩为B的同学有：')
    for k, v in B.items():
        print(f'{k}：{v}', end=' ;')
    print('\n成绩为C的同学有：')
    for k, v in C.items():
        print(f'{k}：{v}', end=' ;')
    print('\n成绩为D的同学有：')
    for k, v in D.items():
        print(f'{k}：{v}', end=' ;')


def score_init():
    stu_name = 'abcdefghijklmnopqrst'
    score = {}
    for i in stu_name:
        score[i] = random.randint(0, 101)
    return score


if __name__ == '__main__':
    rank(score_init())
