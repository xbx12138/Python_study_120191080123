#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:7.py
# author:Asus
# datetime:2021/4/7 17:081
# software: PyCharm
'''
对一篇中文文献, ;利用jieba库,进行词频统计分析找出文章的关键词(取词频最高的前10个词语,作为文章的关键字);
'''
# import module your need
import jieba

seg_list = jieba.cut("全民制作人们大家好我是练习时长两年半的个人练习生蔡徐坤我喜欢唱跳rap篮球")  # 默认是精确模式
jieba.suggest_freq('蔡徐坤', True)
print("/".join(seg_list))
