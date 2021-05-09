#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:4.py
# author:Asus
# datetime:2021/5/9 12:35
# software: PyCharm
'''
四 .封装一个学生类，有姓名，有年龄，有性别，有英语成绩，数学成绩，语文成绩，
      封装方法，求单个学生的总分，平均分，以及打印学生的信息。
'''


# import module your need


class Student:
    name = ''
    age = 0
    sex = '男'
    score = [0.0, 0.0, 0.0]

    def __init__(self, name, age, sex, score):
        self.name = name
        self.age = age
        self.sex = sex
        self.score = score

    def Sum_score(self):
        sum=0
        for i in self.score:
            sum+=i
        return sum

    def Avg_score(self):
        return self.Sum_score()/3


    def getInfo(self):
        print(f'姓名：{self.name}\n年龄：{self.age}\n性别：{self.sex}\n')

if __name__ == '__main__':
    score1=[98,90,95]
    s=Student('小明',20,'男',score1)
    s.getInfo()
    print(f'{s.name}的总分：{s.Sum_score()}')
    print(f'{s.name}的平均分：%.2f'%s.Avg_score())