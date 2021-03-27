#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_dir.py
# author:Asus
# datetime:2021/3/27 10:20
# software: PyCharm
'''
this is functiondescription
'''
# import module your need
import os
from datetime import datetime
print(os.listdir())
# listdir() 打印目录下所有文件的名称
print(datetime.fromtimestamp(os.path.getmtime('do_package.py')))
