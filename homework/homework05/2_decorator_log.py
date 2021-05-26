#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2.py
# author:Asus
# datetime:2021/4/24 12:16
# software: PyCharm
'''
2  编写一个装饰器，能记录其他函数调用的日志，将日志写入到文件中；
'''
# import module your need

import functools
import time
import datetime


def log(func):
    @functools.wraps(func)
    def wrapper(*args, **kw):
        with open('./2/log.txt', 'a', encoding='utf-8')as f:
            date = datetime.datetime.fromtimestamp(time.time())
            call_time = date.strftime('%Y/%m/%d %H:%M')
            log_content = call_time + ' call ' + func.__name__+'\n'
            f.write(log_content)
        return func(*args, **kw)

    return wrapper


@log
def test():
    print('Hello')


if __name__ == '__main__':
    test()
