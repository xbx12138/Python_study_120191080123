#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_reg_test.py
# author:Asus
# datetime:2021/6/5 11:57
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

import re

line=input()
li='哈哈'
match=re.match('^[\u4e00-\u9fa5_a-zA-Z0-9 for _ in li]+$',line)

if match:
    print('!!!')