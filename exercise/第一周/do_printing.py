#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_printing.py
# author:Asus
# datetime:2021/3/7 16:48
# software: PyCharm
'''
随堂练习1:
   在idle交互环境中，输入以下，并观察结果：
   print('hellp\nkitty')；
   print('hello\tkitty')
   print('hello：\'kitty\'','\"boy\"')
   print(r'hello："kitty"')
   print('AAA',end='*')
   print('CCC',end='--')


练习2：打印以下效果：
亲爱的XXX:
   请点击链接激活用户：激活用户
'''
# import module your need

if __name__ == "__main__":
    print('hellp\nkitty')
    print('hello\tkitty')
    print('hello：\'kitty\'', '\"boy\"')
    print(r'hello："kitty"')
    print('AAA', end='*')
    print('CCC', end='--')
    print()
    name = 'xbx12138'
    print('亲爱的', end='')
    print(name,end=':\n')
    print('\t请点击链接激活用户：激活用户')
