#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_cal.py
# author:Asus
# datetime:2021/3/15 14:08
# software: PyCharm
'''
练习:
     定义一个函数,来计算苹果的价格(重量*价格); 通过键盘输入重量和价格,然后调用函数来计算;
'''


# import module your need

def cal(weight, cost):
    return weight * cost


if __name__ == "__main__":
    weight =input("请输入苹果的重量：")
    cost = input("请输入苹果的价格：")
    print(f'总价：{cal(int(weight), int(cost))}')
