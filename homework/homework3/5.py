#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:5.py
# author:Asus
# datetime:2021/4/6 15:12
# software: PyCharm
'''
5 文件编程小项目
'''
# import module your need
import os

if __name__ == '__main__':
    # os.mkdir(os.getcwd(),'5')
    currentdir = os.path.join(os.getcwd(), '5\Blowing in the wind.txt')  # 创建文件
    date = '''How many roads must a man walk down\n\nBefore they call him a man

How many seas must a white dove sail\n\nBefore she sleeps in the sand

How many times must the cannon balls fly\n\nBefore they' re forever banned

The answer my friend is blowing in the wind\n\nThe answer is blowing in the wind'''
    song_name = 'Blowin’ in the wind'
    singer = 'Bob Dylan'
    datetime = ' 1962 by Warner Bros.Inc'
    with open(currentdir, 'w', encoding='utf-8') as fw:  # 录入内容
        fw.write(date)
    with open(currentdir, 'r+', encoding='utf-8') as fr:  # 插入歌名
        tmp_data = fr.read()
        fr.seek(0)
        fr.write(song_name + '\n' + tmp_data)
    with open(currentdir, 'r+', encoding='utf-8') as fr:  # 插入歌手名
        content = str(fr.readlines())
        pos = content.find(song_name) + len(song_name);
        with open(currentdir,'w+',encoding='utf-8') as fw:
            content=content[:pos]+'   '+singer+content[pos:]
            fw.writelines(content)
