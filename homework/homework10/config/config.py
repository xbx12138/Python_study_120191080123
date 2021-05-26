#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:config.py
# author:Asus
# datetime:2021/5/26 20:31
# software: PyCharm
'''
this is functiondescription
'''
# import module your need


# 数据库连接定义
SQLALCHEMY_DATABASE_URI = "mysql+pymysql://root:001122@localhost:3306/python?charset=utf8"

# 数据库连接池初始化的容量
POOL_SIZE = 5

# 连接池最大溢出容量，该容量+初始容量=最大容量。超出会堵塞等待，等待时间为timeout参数值默认30
MAX_OVERFLOW = 10