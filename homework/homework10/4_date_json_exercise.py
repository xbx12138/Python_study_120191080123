#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:4_date_json.py
# author:Asus
# datetime:2021/5/26 23:03
# software: PyCharm
'''
数据序列化和处理练习；
1 打印输出，年龄大于20岁的人员名单；
2 向列表中新增数据；
3 统计男生和女生的人数；
'''
# import module your need

import json


def display(dict_stu):
    print('年龄大于20岁的人员名单:')
    for person in dict_stu:
        if int(person['age']) > 20:
            print(f"姓名：{person['name']} 年龄：{person['age']} 性别：{person['genda']}")


def add_date(dict_stu):
    print('新增数据：')
    person = {'name': input('请输入姓名：'), 'age': input('请输入年龄：'), 'genda': input('请输入性别：')}
    dict_stu.append(person)
    with open('res/date_student.json', 'w', encoding='utf-8') as f:
        json.dump(dict_stu, f)


def count_by_sex(dict_stu):
    male = female = 0
    for person in dict_stu:
        if person['genda'] == '男':
            male += 1
        else:
            female += 1
    print(f'共有男生{male}名,女生{female}名.')


if __name__ == '__main__':
    with open('res/date_student.json', 'r', encoding='utf-8') as f:
        dict_stu = json.load(f)
    display(dict_stu)
    #add_date(dict_stu)
    #count_by_sex(dict_stu)
