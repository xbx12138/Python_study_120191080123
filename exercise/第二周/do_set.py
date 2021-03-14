#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:do_set.py
# author:Asus
# datetime:2021/3/14 20:35
# software: PyCharm
'''
练习:
      定义一个集合类型的变量(用2种方法初始化),然后进行相应的 元素的操作;
'''
# import module your need

a={'xbx',123,'sksk','a','r','g','h'}
b=set('arfhsdauoid')
print(f'a:{a}')
print(f'b:{b}')
print(f'a-b:{a-b}')
print(f'a|b:{a|b}')
print(f'a&b:{a&b}')
print(f'a^b:{a^b}')

thisset={'1','2','3'}
thisset.add('4')
print(f'add:{thisset}')
thisset.update('5','6')
print(f'update:{thisset}')
thisset.remove('1')
print(f'remove:{thisset}')

print(f'len:{len(thisset)}')

