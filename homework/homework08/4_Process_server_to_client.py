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
import sys
from multiprocessing import Process, Queue
import os, time, random


# 写数据进程执行的代码:
def write(q, fn):
    sys.stdin = os.fdopen(fn)
    message = input('发送消息：')
    q.put(message)


# 读数据进程执行的代码:
def read(q):
    while True:
        if not q.empty():
            value = q.get(True)
            print(f'发来消息：{value}')
        else:
            break


if __name__ == '__main__':
    # 父进程创建Queue，并传给各个子进程：
    q = Queue()
    fn = sys.stdin.fileno()
    while True:
        pw = Process(target=write, args=(q,fn))
        pr = Process(target=read, args=(q,))
        # 启动子进程pw，写入:
        pw.start()
        # 等待pw结束:
        pw.join()
        # 启动子进程pr，读取:
        pr.start()
        pr.join()
        # pr进程里是死循环，无法等待其结束，只能强行终止:

