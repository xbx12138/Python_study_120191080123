#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:04.py
# author:Asus
# datetime:2021/3/31 21:25
# software: PyCharm
'''
4  写函数，统计字符串中有几个字母，几个数字，几个空格，几个其他字符，并返回结果;
'''
# import module your need

def count(str):
    Num_ch=Num_num=Num_space=Num_char=0
    for i in str:
        if i.isdigit():
            Num_num+=1
        elif i.isalnum():
            Num_ch+=1
        elif i == ' ':
            Num_space+=1
        else:
            Num_char+=1
    return Num_ch,Num_num,Num_space,Num_char;
if __name__=='__main__':
    str=input('请输入字符串：')
    counts=count(str)
    print(f'共有字母{counts[0]}个，数字{counts[1]}个，空格{counts[2]}个，其他字符{counts[3]}个。')