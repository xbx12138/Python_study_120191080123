#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:9.py
# author:Asus
# datetime:2021/4/24 11:59
# software: PyCharm
'''
9 从网络上下载一张图片，保存到计算机的指定目录；（requests和os模块)
'''
# import module your need

import requests

url = 'https://www.runoob.com/wp-content/uploads/2014/05/python3.png'
html = requests.get(url)

with open('./9/1.png', 'wb') as f:
    f.write(html.content)
