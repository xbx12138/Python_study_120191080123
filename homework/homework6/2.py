#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2.py
# author:Asus
# datetime:2021/5/8 17:40
# software: PyCharm
'''
二 定义一个学生Student类。有下面的类属性：
1 姓名 name
2 年龄 age
3 成绩 score（语文，数学，英语) [每课成绩的类型为整数]
类方法：
1 获取学生的姓名：get_name() 返回类型:str
2 获取学生的年龄：get_age() 返回类型:int
3 返回3门科目中最高的分数。get_course() 返回类型:int
写好类以后，可以定义2个同学测试下:
'''
# import module your need

class Student:
    __name=''
    __age=0
    __score=[0,0,0]
    def __init__(self,name,age,score):
        self.__name=name
        self.__age=age
        self.__score=score

    def get_name(self):
        return self.__name

    def get_age(self):
        return self.__age

    def get_course(self):
        Max=0
        for i in range(0,3):
            score=self.__score[i]
            if Max<score:
                Max=score
        return int(Max)

if __name__ == '__main__':
    score1=[95,99,92]
    score2=[92,93,90]
    s1=Student('小米',18,score1)
    s2=Student('小红',20,score2)
    print(f'name:{s1.get_name()} age:{s1.get_age()} MAX_SCORE:{s1.get_course()}')
    print(f'name:{s2.get_name()} age:{s2.get_age()} MAX_SCORE:{s2.get_course()}')