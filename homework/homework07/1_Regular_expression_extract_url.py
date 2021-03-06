#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:1_Regular_expression_extract_url.py
# author:Asus
# datetime:2021/5/22 11:36
# software: PyCharm
'''
1 给定一个文件，请用正则表达式，逐行匹配提取其中的URL链接信息，并保存到另外一个文件中；
 提示，文件有1000行，注意控制每次读取的行数；
'''
# import module your need

import re


def main():
    with open('1/webspiderUrl.txt', 'r', encoding='utf-8') as fr:
        with open('1/Urls.txt', 'a', encoding='utf-8') as fw:
            weblines = fr.readlines()
            for line in weblines:
                matchUrl = re.search(r'(https?|ftp|file)://[-A-Za-z0-9+&@#/%?=~_|!:,.;]+[-A-Za-z0-9+&@#/%=~_|]', line)
                if matchUrl:
                    fw.write(matchUrl.group()+'\n')


if __name__ == "__main__":
    main()
