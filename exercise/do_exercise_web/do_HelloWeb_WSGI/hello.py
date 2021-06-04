#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:hello.py
# author:Asus
# datetime:2021/6/1 15:47
# software: PyCharm
'''
this is functiondescription
'''


# import module your need

def application(environ, start_response):
    start_response('200 OK', [('Content-Type', 'text/html')])
    body = '<h1>Hello ,%s!</h1>' % (environ['PATH_INFO'][1:] or 'Web')
    return [body.encode('utf-8')]
