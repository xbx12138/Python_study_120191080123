#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:fight.py
# author:Asus
# datetime:2021/5/9 13:09
# software: PyCharm
'''
3   对战规则:
     A  随机决定,谁先开始攻击;
     B  一方攻击完毕后, 另外一方再开始攻击;
        攻击的目标是随机的(比如, 人要打狗了, 随机找一条血不为0的狗攻击);
     C  每次攻击, 双方只能安排一个人,或者一条狗进行攻击;
'''
# import module your need
import Dog
import Person
import random


class fight:
    num_Person = 0
    num_Dog = 0
    persons = []
    dogs = []

    def __init__(self, persons, dogs):
        self.num_Person = persons
        for i in range(0, persons):
            p = Person()
            self.persons.append(p)
        self.num_Dog = dogs
        for i in range(0, dogs):
            d = Dog()
            self.dogs.append(d)

    def end(self):
        flag_person = False
        for i in self.persons:
            if i.__islive():
                flag_person = True
        flag_dog = False
        for i in self.dogs:
            if i.__islive():
                flag_dog = True
        if flag_person and flag_dog:
            return True
        elif flag_person:
            print('人活到了最后！')
            return False
        elif flag_dog:
            print('狗活到了最后！')
            return False

    def p_hit_d(self):
        

    def d_hit_p(self):
        d = 1

    def start(self):
        flag_hit = True
        if random.randint(0, 1) == 1:
            flag_hit = False
        while self.end():
            if flag_hit:
                self.p_hit_d()
                flag_hit = False
            else:
                self.d_hit_p()
                flag_hit = True
