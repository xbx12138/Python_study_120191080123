#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:_init_.py
# author:Asus
# datetime:2021/5/25 17:50
# software: PyCharm
'''
this is functiondescription
'''
# import module your need


from sqlalchemy import create_engine
from sqlalchemy.orm import sessionmaker

from config import config

# 创建引擎
engine = create_engine(config.SQLALCHEMY_DATABASE_URI)

# 创建会话对象
Session = sessionmaker(bind=engine)

# 创建会话实例
session = Session()
