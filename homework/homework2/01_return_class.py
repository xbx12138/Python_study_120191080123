#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:01_element_out_search.py
# author:Asus
# datetime:2021/3/25 23:01
# software: PyCharm
'''
1 写函数，判断用户传入的对象（字符串、列表、元组）长度,并返回给调用者。

'''


# import module your need

def fun(a, b, c):
    return (len(a), len(b), len(c))


if __name__ == '__main__':
    a = 'qwertyuio'
    b = [1, 2, 3, 4, 5, 6, 7]
    c = ('z', 'x', 'c', 'v', 'b', 'n')
    x, y, z = fun(a, b, c)
    print(f"字符串的长度：{x},列表的长度：{y},元组的长度：{z}")