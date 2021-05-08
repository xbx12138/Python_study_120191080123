#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3.py
# author:Asus
# datetime:2021/4/24 12:35
# software: PyCharm
'''
3  编写一个装饰器，为多个函数加上认证的功能（必须输入用户的账号密码，才能调用这个函数）
'''
# import module your need

pwd='123456'

def outer(func):
    def inner():
        pwd_1=input('请输入账号密码：');
        if pwd_1==pwd :
            func()
        else:
            print('账号密码有误！！')
    return inner

@outer
def fun():
    print('Hello World!')

if __name__ == '__main__':
    fun()