#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:2_Message_Board.py
# author:Asus
# datetime:2021/5/23 20:08
# software: PyCharm
'''
2  设计一个留言版的表（ID，留言内容，留言人，留言时间，是否删除）
（表名，和字段名自己设计成英文：注意，不要用中文，用中文的直接0分）；
   使用PyMySQL 驱动模块，实现对这个表的增加，删除，修改，查询；数据库操作需要加入异常处理逻辑；
'''
# import module your need


import pymysql


def add(cursor):
    sql_insert = "INSERT INTO `message_board`(ID ,Message_content ,author ,Message_time ,exist) " \
                 "VALUES  ('%s','%s','%s','%s','%s')"


def main():
    db = pymysql.connect(user='root', password='001122', host='localhost', port=3306, database='python',
                         charset="utf8")
    cursor = db.cursor()

    sql = 'SELECT * FROM `message_board` '
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        print(results)
    except:
        print('Error: unable to fetch data')

    db.close()


if __name__ == '__main__':
    main()
