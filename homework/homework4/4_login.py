#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:4.py
# author:Asus
# datetime:2021/4/22 19:47
# software: PyCharm
'''
4  (继续上面的练习) 模拟用户登录:
     5个同学的姓名,账号和密码(加密后的),保存在一个文件上;
    系统提示,请输入登录同学姓名, 正确后,请输入账号, 正确后,提示请输入密码（输入明文）;
    如果都正确,打印提示, 您登录成功(失败);

'''
# import module your need

import hashlib
import json


def log(dict):
    md5=hashlib.md5()
    name = input('请输入登录同学姓名:')
    if name in dict:
        user=input('请输入账号:')
        if dict[name][0]==user:
            pwd=input('请输入密码:')
            md5.update(pwd.encode('utf-8'))
            if dict[name][1]==md5.hexdigest():
                print('登录成功！')
            else:
                print('登录失败！')
        else:
            print('登录失败！')
    else:
        print('登录失败！')


if __name__ == '__main__':
    dict = {}
    with open('3/json_file.json', 'r', encoding='utf-8') as f:
        dict = json.load(f)
    log(dict)
