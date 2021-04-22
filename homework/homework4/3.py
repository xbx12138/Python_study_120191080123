#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3.py
# author:Asus
# datetime:2021/4/22 19:08
# software: PyCharm
'''
3  从键盘输入5个同学的账号和密码,然后将他们的姓名,账号和密码(密码需要加密)保存到一个文件中;
        Tom   admin   XXXXX
        Jack  root    XXXXX

'''
# import module your need
import os
import hashlib
import json

if __name__ == '__main__':
    acounts = {}
    for i in range(0, 5):
        name_stu = input('请输入学生姓名：')
        user_stu = input('请输入账号：')
        pwd_stu = input('请输入密码')
        md5 = hashlib.md5()
        md5.update(pwd_stu.encode('utf-8'))
        pwd_md = md5.hexdigest()
        date = [name_stu, pwd_md]
        acounts[user_stu] = date

    with open('./3/json_file.json', 'w', encoding='utf-8') as f:
        json.dump(acounts, f)
