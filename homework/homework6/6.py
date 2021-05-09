#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:6.py
# author:Asus
# datetime:2021/5/9 15:49
# software: PyCharm
'''
六  用面向对象,实现一个学生Python成绩管理系统;
      学生的信息存储在文件中;学生信息的字段有(班级,学号,姓名, Python成绩)
      实现对学生信息及成绩的增,删,改,查方法;
'''

# import module your need

import json


class Student:
    Students = {}

    def add_stu(self, id_stu, name, classes, score):
        self.Students[id_stu:[name, classes, score]]

    def del_stu(self, id_stu):
        self.Students.pop(id_stu)

    def update_stu(self, id_stu, name, classes, score):
        self.Students[id_stu:[name, classes, score]]

    def search_stu(self, id_stu):
        print(f'学号：{id_stu}\n姓名：{self.Students[id_stu][0]}\n'
              f'班级：{self.Students[id_stu][1]}\nPython成绩：{self.Students[id_stu][2]}')

    def save_stu(self):
        with open('.6/json_stu', 'w') as f:
            json.dump(self.Students, f)

    def load_stu(self):
        with open('.6/json_stu') as f:
            self.Students=json.load(f)


if __name__ == '__main__':
    stu = Student()
    print('学生Python成绩管理系统\n1.增加；\n2.删除；\n3.修改；\n4.查询；\n5.读档；\n6.保存。\n    0.退出')
    flag=int(input('输入功能序号'))
    while flag==0:
        if flag==1:
            print('增加信息：')
            id_stu=input('输入学号：')
            name=input('输入姓名')
            classes=input('输入班级：')
            score=input('输入python成绩：')
            stu.add_stu(id_stu,name,classes,score)
        elif flag==2:
            print('删除信息：')
            id_stu=input('输入需删除学生的学号:')
            stu.del_stu(id_stu)
        elif flag==3:
            print('修改信息：')
            id_stu=input('输入需修改信息学生的学号：')
            print('请输入修改后的信息：')
            name = input('输入姓名')
            classes = input('输入班级：')
            score = input('输入python成绩：')
            stu.update_stu(id_stu,name,classes,score)
        elif flag==4:
            print('查询信息：')
            id_stu = input('输入需查询信息学生的学号：')
            stu.search_stu(id_stu)
        elif flag==5:
            print('保存')
            stu.save_stu()
        flag=int(input('输入功能序号'))

