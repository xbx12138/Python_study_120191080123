#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:Dog.py
# author:Asus
# datetime:2021/5/9 12:52
# software: PyCharm
'''
狗的攻击力为 15; 初始化血为80;
狗被人打了也掉血
狗被打一次,攻击力降低3

'''
# import module your need
import Person


class Dog:
    __HP = 0
    __Ad = 0

    def __init__(self):
        self.__HP = 80
        self.__Ad = 15

    def hit(self, target):
        target.injured(self.__Ad)

    def injured(self, ad):
        self.__HP -= ad
        if self.__Ad >= 3:
            self.__Ad -= 3
        if self.__HP <= 0:
            print('————————————————\n一只狗已被击杀！\n————————————————\n')
            self.__HP = 0

    def islive(self):
        if self.__HP > 0:
            return True
        else:
            return False

    def getHp(self):
        return self.__HP
