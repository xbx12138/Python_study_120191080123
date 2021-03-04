#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_reserver.py
# author:Asus
# datetime:2021/3/4 15:17
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 课堂练习：
# 输入一个字符串，比如 abcdef；1 通过字符串切片方式反向输出；2 存放到列表中，然后反向输出：fedcba

def reverseStr(input):
    print(input[::-1])

def reverselist(input):
    inputlist=list(input)
    inputlist=inputlist[-1::-1]
    return inputlist

if __name__=="__main__":
    str = "abcdef"
    reverseStr(str)
    rl=reverselist(str)
    print(rl)