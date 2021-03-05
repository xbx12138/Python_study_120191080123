#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:09.py
# author:Asus
# datetime:2021/3/5 17:36
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 9 设计一个猜数字 游戏；最多只能猜测N次，在N次之内猜不出，就退出程序，提示猜测失败；

import random

if __name__ == "__main__":
    key = random.randint(1, 20)
    N = random.randint(5, 10)
    n = 0
    print('猜数字，范围在1~20之间,最多猜测', N, '次')
    while n < N:
        print('还剩', N - n, '次。')
        k = int(input('请输入:'))
        if k == key:
            print('恭喜您猜对了！')
            break
        else:
            print('您猜错了！')
            n += 1
