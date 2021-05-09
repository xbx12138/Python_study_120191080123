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
    __HP = 80
    __Ad = 15

    def hit(self, target):
        target.injured(self.__Ad)

    def injured(self, ad):
        self.__HP -= ad
        self.__Ad -= 3
        if self.__HP <= 0:
            print('一只狗已被击杀！')

    def islive(self):
        if self.__HP > 0:
            return True
        else:
            return False