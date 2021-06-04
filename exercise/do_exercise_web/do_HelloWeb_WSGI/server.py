#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:server.py
# author:Asus
# datetime:2021/6/1 15:51
# software: PyCharm
'''
this is functiondescription
'''
# import module your need


from wsgiref.simple_server import make_server
from hello import application

if __name__ == '__main__':
    httpd = make_server('', 7788, application)
    print('Servring HTTP on port 7788...')
    httpd.serve_forever()