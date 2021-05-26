#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:Person.py
# author:Asus
# datetime:2021/5/9 12:52
# software: PyCharm
'''
人的打击力为10;  初始化血为100;
人被狗咬了会掉血
人被咬一次,打击力降低2;
'''

# import module your need
import Dog


class Person:
    __HP = 0
    __Ad = 0

    def __init__(self):
        self.__HP = 100
        self.__Ad = 10

    def hit(self, target):
        target.injured(self.__Ad)

    def injured(self, ad):
        self.__HP -= ad
        if self.__Ad >= 2:
            self.__Ad -= 2
        if self.__HP <= 0:
            print('————————————————\n一人已被击杀！\n————————————————\n')
            self.__HP = 0

    def islive(self):
        if self.__HP > 0:
            return True
        else:
            return False

    def getHp(self):
        return self.__HP
