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

from pdfminer.pdfparser import PDFParser, PDFDocument
from pdfminer.pdfinterp import PDFResourceManager, PDFPageInterpreter
from pdfminer.converter import PDFPageAggregator
from pdfminer.layout import LTTextBoxHorizontal, LAParams
from pdfminer.pdfinterp import PDFTextExtractionNotAllowed


def parse(text_path):
    '''解析PDF文本，并保存到TXT文件中'''
    with open(text_path, 'rb')as fp:
        # 用文件对象创建一个PDF文档分析器
        parser = PDFParser(fp)
    # 创建一个PDF文档
    doc = PDFDocument()
    # 连接分析器，与文档对象
    parser.set_document(doc)
    doc.set_parser(parser)

    # 提供初始化密码，如果没有密码，就创建一个空的字符串
    doc.initialize()

    # 检测文档是否提供txt转换，不提供就忽略
    if not doc.is_extractable:
        raise PDFTextExtractionNotAllowed
    else:
        # 创建PDF，资源管理器，来共享资源
        rsrcmgr = PDFResourceManager()
        # 创建一个PDF设备对象
        laparams = LAParams()
        device = PDFPageAggregator(rsrcmgr, laparams=laparams)
        # 创建一个PDF解释其对象
        interpreter = PDFPageInterpreter(rsrcmgr, device)

        # 循环遍历列表，每次处理一个page内容
        # doc.get_pages() 获取page列表
        for page in doc.get_pages():
            interpreter.process_page(page)
            # 接受该页面的LTPage对象
            layout = device.get_result()
            # 这里layout是一个LTPage对象 里面存放着 这个page解析出的各种对象
            # 一般包括LTTextBox, LTFigure, LTImage, LTTextBoxHorizontal 等等
            # 想要获取文本就获得对象的text属性，
            for x in layout:
                if (isinstance(x, LTTextBoxHorizontal)):
                    with open(r'./7/1.txt', 'a', encoding='utf-8') as f:
                        results = x.get_text()
                        f.write(results + "\n")


def bubble_sort(lists):
    count = len(lists)
    for i in range(0, count):
        for j in range(i + 1, count):
            if lists[i][1] < lists[j][1]:
                lists[i], lists[j] = lists[j], lists[i]
    return lists


if __name__ == '__main__':
    pdf_path = r'./7/热成像技术在生物学教学中的应用_龙仲英.pdf'
    parse(pdf_path)
    with open('./7/1.txt', 'r', encoding='utf-8')as fr:
        text = fr.read()

    for ch in '\n !@#$%^&*()_+~`";:,<.>/?\|=-[]{}（）”。，《》？、【】：；‘°×':
        text = text.replace(ch, ',')
    txtlist = jieba.lcut(text)
    words = {}
    wordlist = []
    for word in txtlist:
        if word in words:
            words[word] += 1
        else:
            words[word] = 1
    for k, v in words.items():
        tup = (k, v)
        wordlist.append(tup)
    bubble_sort(wordlist)
    for i in range(1, 11):
        print(f'{i}: {wordlist[i][0]} 次数：{wordlist[i][1]}')
