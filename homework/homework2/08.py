#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:08.py
# author:Asus
# datetime:2021/4/4 11:25
# software: PyCharm
'''
8  请用Python定义一个函数，给定一个字符串，找出该字符串中出现次数最多的那个字符，并打印出该字符及其出现的次数。
 例如，输入 aaaabbc，输出：a:4
'''


# import module your need

def counter(str):
    count = {}
    num_max = 0
    char = ' '
    for i in str:
        if i in count:
            count[i] += 1
            if count[i] > num_max:
                num_max = count[i]
                char = i
        else:
            count[i] = 1
    print(f'{char}:{num_max}')


if __name__ == '__main__':
    counter(input('请输入字符串：'))
