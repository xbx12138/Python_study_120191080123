#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:08.py
# author:Asus
# datetime:2021/3/5 14:30
# software: PyCharm
'''
this is functiondescription
'''


# import module your need

# 8 设计一个数据结构，用来存放10个员工的信息并初始化，每个员工信息包括：工号，姓名，工龄，工资；  将这10个员工，按照工资从高到低打印输出；
#    提示：可以组合使用我们的序列数据类型；

def sorting(e):
    key = []
    for k in e[0].keys():
        key.append(k)
    n = len(key)
    for i in range(1, n):
        temp = e[2][key[i]]
        k = key[i]
        j = i - 1
        while j >= 0 and e[2][key[j]] < temp:
            key[j + 1] = key[j]
            j -= 1
        key[j + 1] = k
    return key


if __name__ == "__main__":
    name = {'001': '老大', '002': '两仪', '003': '三元', '004': '四春', '005': '五福', '006': '六花', '007': '七娣', '008': '老八',
            '009': '九妹', '010': '老十'}
    age = {'001': 12, '002': 12, '003': 11, '004': 10, '005': 9, '006': 6, '007': 7, '008': 8,
           '009': 5, '010': 3}
    wage = {'001': 12000, '002': 18000, '003': 15000, '004': 8000, '005': 10000, '006': 6000,
            '007': 11000, '008': 5000, '009': 13000, '010': 4000}
    employees = [name, age, wage]
    sort = sorting(employees)
    print('姓名  工龄   工资')
    for key in sort:
        print(employees[0][key], ' ', employees[1][key], ' ', employees[2][key])
