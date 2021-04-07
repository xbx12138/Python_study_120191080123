#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3.py
# author:Asus
# datetime:2021/4/4 16:51
# software: PyCharm
'''
3 编写一个程序，读取文件中保存的10个学生成绩名单信息(学号,姓名, Python课程分数);
 然后按照分数从高到低进行排序输出
'''


# import module your need

def sort(nums):  # 冒泡排序
    for i in range(len(nums) - 1):
        for j in range(len(nums) - i - 1):
            if nums[j][2] < nums[j + 1][2]:
                nums[j], nums[j + 1] = nums[j + 1], nums[j]
    return nums


if __name__ == '__main__':
    with open('./3/score.txt', 'r', encoding='utf-8') as fr:
        Head = fr.readline().strip().split('    ')
        # 将信息存储在二维列表
        a = []
        for line in fr.readlines():
            b = []
            for i in line.strip().split('    '):
                b.append(i)
            a.append(b)
        # 将分数转化
        for i in a:
            i[2] = float(i[2])

        sort(a)
        for i in Head:
            print(i, end='    ')
        for i in a:
            print('\n')
            for j in i:
                print(j, end='    ')

