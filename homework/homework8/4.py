#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:4.py
# author:Asus
# datetime:2021/5/18 22:00
# software: PyCharm
'''
4 多进程通讯：
  编写一个简单的聊天程序；其中一个进程发送文字聊天消息（从键盘输入文字消息）；
   另外一个进程接收并打印消息；
'''
# import module your need
from multiprocessing import Manager,Pool

import os, time, random


def long_time_task(name):
    print('Run task %s (%s)...' % (name, os.getpid()))
    start = time.time()
    time.sleep(random.random() * 3)
    end = time.time()
    print('Task %s runs %0.2f seconds.' % (name, (end - start)))

if __name__=='__main__':
    print('Parent process %s.' % os.getpid())
    p = Pool(4)
    for i in range(5):
        p.apply_async(long_time_task, args=(i,))
    print('Waiting for all subprocesses done...')
    p.close()
    p.join()
    print('All subprocesses done.')
