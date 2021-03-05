#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:10.py
# author:Asus
# datetime:2021/3/5 17:55
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

# 10  给定一段英文文本，统计每个单词出现的次数；打印输出，按照词频从高到低输出：
#    提示：可以用字典来统计：key 是单词，value 是单词出现次数；
#     先创建一个字典，然后遍历刚刚取出的单词列表，接着做一个判断： 如果字典中 key 已经出现了这个单词，
#     那么它对应的 value ，也就是出现次数就 +1； 如果这个单词没出现过，就直接 插入这个单词及 value 为 1 到 字典中；


if __name__ == "__main__":
    text = input('请输入英文文本:')
    text = text.replace(', ', ' ')
    text = text.replace('. ', ' ')
    text = text.lower()  # 大写字母变小写
    textList = text.split(' ')
    words = {}
    for word in textList:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    wordList = list(words)
    numberList = list(words.values())
    # 排序
    n = len(wordList)
    for i in range(1, n):
        tempNum = numberList[i]
        tempWord = wordList[i]
        j = i - 1
        while j >= 0 and numberList[j] < tempNum:
            wordList[j + 1] = wordList[j]
            numberList[j + 1] = numberList[j]
            j -= 1
        wordList[j + 1] = tempWord
        numberList[j + 1] = tempNum

    for i in range(1, n):
        print(wordList[i], '出现次数:', numberList[i])
