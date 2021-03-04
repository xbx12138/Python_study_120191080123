#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:1.py
# author:Asus
# datetime:2021/3/4 16:19
# software: PyCharm
'''
this is functiondescription
'''


# import module your need

# 1 元素输出和查找：  请输出0-50之间的奇数，偶数，质数；能同时被2和3整除的数；

if __name__ == "__main__":
    oddNum = []  # 奇数列表
    evenNum = []  # 偶数列表
    primeNum = []  # 质数列表
    twothreeNum = []  # 能同时被2和3整除的数列表
    for i in range(0, 51):
        if i % 2 == 1:
            oddNum.append(i)
        else:
            evenNum.append(i)
        if i % 6 == 0:
            twothreeNum.append(i)
        if i > 1:
            flag = True
            for j in range(2, i):
                if i % j == 0:
                    flag = False
                    break
            if flag:
                primeNum.append(i)

    print("奇数:", oddNum)
    print("偶数:", evenNum)
    print("质数:", primeNum)
    print("能同时被2和3整除的数:", twothreeNum)
