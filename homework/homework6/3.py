#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:3.py
# author:Asus
# datetime:2021/5/8 18:45
# software: PyCharm
'''
三、定义一个字典类：dictclass。完成下面的功能：
dict = dictclass({你需要操作的字典对象})
1 删除某个key
del_dict(key)
2 判断某个键是否在字典里，如果在返回键对应的值，不存在则返回"not found"
get_dict(key)
3 返回键组成的列表：返回类型;(list)
get_key()
4 合并字典，并且返回合并后字典的values组成的列表。返回类型:(list)
update_dict({要合并的字典})
'''


# import module your need

class dictclass:
    __dict = {}

    def __init__(self, dict):
        self.__dict = dict

    def del_dict(self, key):
        self.__dict.pop(key)

    def get_dict(self, key):
        if key in self.__dict:
            return self.__dict[key]
        else:
            return 'not found'

    def get_key(self):
        key = []
        for k, v in self.__dict.items():
            key.append(k)
        return key

    def update_dict(self, dict1):
        d = {k: v for d in [self.__dict, dict1] for k, v in d.items()}
        self.__dict = d
        value = []
        for k, v in self.__dict.items():
            value.append(v)


if __name__ == '__main__':
    dic = {4: 'q', 5: 'r', 6: 'y'}
    d = dictclass({1: 'a', 2: 's', 3: 'q'})
    d.del_dict(1)
    print(d.get_dict(2))
    print(d.get_key())
    d.update_dict(dic)
    print(d.get_key())
