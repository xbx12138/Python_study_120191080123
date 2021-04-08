#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:8.py
# author:Asus
# datetime:2021/4/8 19:15
# software: PyCharm
'''
8 在2个文件中存放了英文计算机技术文章(可以选择2篇关于Python技术文件操作处理技巧的2篇英文技术文章),
 请读取文章内容,进行词频的统计;并分别输出统计结果到另外的文件存放;
 比较这2篇文章的相似度
 (如果词频最高的前10个词,重复了5个,相似度就是50%;重复了6个,相似度就是60% ,......);
'''

# import module your need

import os


def getText(path):  # 提取信息
    with open(path, 'r', encoding='utf-8') as fr:
        txt = fr.read()
        txt = txt.lower().replace('\n', ' ')
        for ch in '!@#$%^&*()_+~`";:,<.>/?\|=-[]{}':
            txt = txt.replace(ch, ' ')
        return txt


def bubble_sort(lists):  # 冒泡排序
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i][1] < lists[j][1]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


def storage(st_list, path):  # 存储词频
    path_word = os.path.split(path)[0]+'\\'+os.path.splitext(os.path.split(path)[1])[0] + '_word_frequency'+os.path.splitext(os.path.split(path)[1])[1]
    with open(path_word, 'w', encoding='utf-8')as fw:
        fw.write(str(st_list))


def count(path):
    words = {}
    wordlist = []
    plist = []
    txt = getText(path)
    txtlist = txt.split(' ')
    for word in txtlist:
        if word in words:
            words[word] += 1
        elif word != '':
            words[word] = 1
    for k, v in words.items():
        tup = (k, v)
        wordlist.append(tup)
    bubble_sort(wordlist)
    storage(wordlist, path)

    # for i in range(0, 10):
    #     print(f'{i + 1}: {wordlist[i][0]} 次数：{wordlist[i][1]}')
    for i in range(0, 10):
        plist.append(wordlist[i][0])
    return plist  # 返回词频前十的单词


def solve(path1, path2):
    set1 = set(count(path1))  # 以集合的方式存储 高频词，方便求交集
    set2 = set(count(path2))
    return len(set1.intersection(set2))  # 交集的长度


if __name__ == '__main__':
    p1 = r'.\8\1.txt'
    p2 = r'.\8\2.txt'

    print(f'两篇文章的相似度为{solve(p1, p2)}0%。')
