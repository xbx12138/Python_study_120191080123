#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:get.py
# author:Asus
# datetime:2021/5/22 10:30
# software: PyCharm
'''
需要把目录标记为源
'''
# import module your need

import socket
import datetime


def get_ip():
    """用来搞到IP"""
    host = socket.gethostname()
    ip = socket.gethostbyname(host)
    return ip


def get_time():
    """得到发送时间"""
    now = datetime.datetime.now()
    send_time = now.strftime("%Y-%m-%d %H:%M:%S")
    return send_time
