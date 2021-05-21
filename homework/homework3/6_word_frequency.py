#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:6.py
# author:Asus
# datetime:2021/4/7 16:03
# software: PyCharm
'''
6 对一篇英文小说，进行词频统计，输出前20个出现频率最高的单词；
英文小说"老人与海"
链接：https://pan.baidu.com/s/1goqK3zF8VBUFuD_2ezfZ7Q 提取码：mv04
提示： 1 可以先定义一个函数，专门来处理英文文章的读取问题；
读取时，解决大小写问题，以及标点符号问题（如，将标点符号都替换成空格）；
'''


# import module your need

def getText():
    with open('./6/《老人与海》[英文版].txt', 'r', encoding='utf-8') as fr:
        txt = fr.read()
        txt = txt.lower().replace('\n', ' ')
        for ch in '!@#$%^&*()_+~`";:,<.>/?\|=-[]{}':
            txt = txt.replace(ch, ' ')
        return txt


def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i][1] < lists[j][1]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


if __name__ == '__main__':
    words = {}
    wordlist = []
    txt = getText()
    txtlist = txt.split(' ')
    for word in txtlist:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    for k, v in words.items():
        tup = (k, v)
        wordlist.append(tup)

    bubble_sort(wordlist)
    for i in range(1, 21):
        print(f'{i}: {wordlist[i][0]} 次数：{wordlist[i][1]}')
