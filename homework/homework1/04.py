#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:04.py
# author:Asus
# datetime:2021/3/4 18:33
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 4  判断用户输入的年份是否为闰年

if __name__ == "__main__":
    year = int(input('请输入年份:'))

    flag = True
    if year % 100 == 0:
        if year % 400 != 0:
            flag = False
    elif year % 4 != 0:
        flag = False

    if flag:
        print(year, "是闰年。")
    else:
        print(year, "不是闰年。")
