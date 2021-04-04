#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:1.py
# author:Asus
# datetime:2021/4/4 15:30
# software: PyCharm
'''
1 写一个程序，读取键盘输入的任意行文字信息，当输入空行时结束输入，
将读入的字符串存于列表;然后将列表里面的内容写入到文件input.txt中；
'''
# import module your need


if __name__ == '__main__':
    strList = []
    s = input("请输入：")
    while not s == '':
        strList.append(s)
        s = input()
    with open('./1/input.txt', 'a+', encoding='utf-8') as fw:
        for i in strList:
            fw.write(i+'\n')
