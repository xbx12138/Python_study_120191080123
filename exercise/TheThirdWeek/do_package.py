#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_package.py
# author:Asus
# datetime:2021/3/25 23:59
# software: PyCharm
'''
练习:
   使用不定长参数定义一个函数;实现对输入数据的封装(封装成一个列表和字典),然后打印输出;

'''


# import module your need
def package_list(*args):
    print(args)


def package_dict(**args):
    print(args)


if __name__ == '__main__':
    package_list(1, 6, 5, 9, 4, 5, 6, 1, 45, 5)
    package_dict(a=1, b=2, c=3)
