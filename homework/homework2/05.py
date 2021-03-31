#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:05.py
# author:Asus
# datetime:2021/3/31 22:04
# software: PyCharm
'''
5  写函数，检查传入字典的每一个value长度，如果大于2，那么仅保留前两个长度的内容，并将新内容返回给调用者;
'''


# import module your need

def keep_Two(dicts):
    for k, v in dicts:
        if v.isdigit():
            length = 0
            num = v
            while num != 0:
                num //= 10
                length += 1
            if length > 2:
                length -= 2
                while length > 0:
                    v //= 10
                dicts[k] = v


if __name__ == '__main__':
    dicts = {1: 'q', 2: 233, 3: 'e'}
    keep_Two(dicts)
    print(dicts[2])
