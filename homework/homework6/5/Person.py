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
    __HP = 100
    __Ad = 10

    def hit(self, target):
        target.injured(self.__Ad)

    def injured(self, ad):
        self.__HP -= ad
        self.__Ad -= 2
        if self.__HP <= 0:
            print('一人已被击杀！')

    def islive(self):
        if self.__HP > 0:
            return True
        else:
            return False
