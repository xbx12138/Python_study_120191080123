#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2.py
# author:Asus
# datetime:2021/4/4 15:57
# software: PyCharm
'''
2 写一个程序，从input.txt中读取之前输入的数据，存入列表中，再加上行号打印显示；格式如下
 1.#第一行： xxxx
 2.#第二行： xxxx
'''
# import module your need


if __name__ == '__main__':
    char = ['', '一', '二', '三', '四', '五', '六', '七', '八', '九', '十']
    strList = []
    i = 0
    with open('./1/input.txt', 'r', encoding='utf-8') as fr:
        for line in fr.readlines():
            strList.append(line.strip())

    for str1 in strList:
        i += 1
        rank = ''
        if i % 10 == 0:
            if i / 10 == 1:
                rank = char[10]
            else:
                rank = char[int(i / 10)] + char[10]
        elif 1 <= i < 10:
            rank = char[i]
        elif 10 < i < 100:
            if i / 10 == 1:
                rank = char[10] + char[i % 10]
            else:
                rank = char[int(i / 10)] + char[10] + char[i % 10]
        print(f'{i}.第{rank}行：{str1}')
