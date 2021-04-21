#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2.py
# author:Asus
# datetime:2021/4/21 22:02
# software: PyCharm
'''
2 定义一个函数，判断一个输入的日期，是当年的第几周，周几？
将程序改写一下，能针对我们学校的校历时间进行计算
（校历第1周，2月17-2月23；校历第27周，8月17-8月23；）；

'''
# import module your need


from datetime import datetime

month_ = [0, 31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]
week = ['', '星期一', '星期二', '星期三', '星期四', '星期五', '星期六', '星期天']


def fun(month, day):
    value = 0
    if month == 3:
        value += day
    else:
        #value += 31
        for i in range(3, month):
            value += month_[i]
        value += day

    print(f'校历第{int(value / 7)+1}周，{week[datetime.now().weekday()+1]}')


if __name__ == "__main__":
    month = int(input('输入月份：'))
    day = int(input('输入日期：'))
    fun(month, day)
