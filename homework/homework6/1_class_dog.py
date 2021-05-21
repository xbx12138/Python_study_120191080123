#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:1.py
# author:Asus
# datetime:2021/5/8 17:15
# software: PyCharm
'''
一、定义一个狗类,里面有一个 列表成员变量(列表的元素是字典), 分别记录了 3种颜色的狗的颜色, 数量,和价格;
       实现狗的买卖交易方法;  打印输出经过2-3次买卖方法后,剩下的各类狗的数量;
'''


# import module your need


class Dog:
    __dogs = [{'color': 'white', 'num': 7, 'price': 1000},
              {'color': 'yellow', 'num': 9, 'price': 800},
              {'color': 'black', 'num': 6, 'price': 1200}]
    def sell(self,id,num):
        if self.__dogs[id]['num']>=num:
            self.__dogs[id]['num']-=num
            print('购买成功！')
        else :
            print('剩余狗的数量不足！')
    def getInfo(self):
        for i in range(0,3):
            num=self.__dogs[i]['num']
            print(f'第{i}种狗狗剩余数量：{num}只；')

if __name__ == '__main__':
    D=Dog()
    D.sell(0,3)
    D.sell(1,6)
    D.sell(2,4)
    D.getInfo()