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
from datetime import datetime


def add(db):
    cursor = db.cursor()
    Message_content = input('输入留言内容：')
    author = input('输入你的姓名：')
    sql_insert = "INSERT INTO `message_board`(Message_content ,author ,Message_time ,exist) " \
                 "VALUES  ('%s','%s','%s','%s')" % (Message_content, author, datetime.now(), 1)
    try:
        cursor.execute(sql_insert)
        db.commit()
        print('提交成功！')
    except:
        db.rollback()
        print('提交失败！')


def delete(db):
    cursor = db.cursor()
    #sql_del = '''DELETE FROM `message_board` WHERE Message_content = "%s"  ''' % input('输入需删除的留言内容:')
    sql_del = '''UPDATE message_board SET exist = 0 WHERE message_content = "%s" ''' % input('\n输入需删除的留言内容:')
    print(sql_del)
    try:
        cursor.execute(sql_del)
        db.commit()
        print('删除成功！')
    except:
        db.rollback()
        print('删除失败！')


def display(db):
    cursor = db.cursor()
    sql = 'SELECT * FROM `message_board` '
    try:
        cursor.execute(sql)
        results = cursor.fetchall()
        for row in results:
            if row[4] == 0:
                continue
            Message_content = row[1]
            author = row[2]
            Message_time = row[3]
            print(f'{Message_content}  ——{author} {Message_time}')
    except:
        print('Error: unable to fetch data')


def search(db):
    cursor = db.cursor()
    sql_search = '''SELECT * FROM `message_board` WHERE author = "%s" ''' % input('输入查询的留言人：')
    try:
        cursor.execute(sql_search)
        results = cursor.fetchall()
        for row in results:
            if row[4] == 0:
                continue
            Message_content = row[1]
            author = row[2]
            Message_time = row[3]
            print(f'{Message_content}  ——{author} {Message_time}')
    except:
        print('Error: unable to fetch data')


def update(db):
    cursor = db.cursor()
    old_content = input('\n输入需修改的留言：')
    new_content = input('\n输入修改后的留言：')
    sql_update = '''UPDATE message_board SET message_content = "%s" WHERE message_content = "%s" ''' % (new_content, old_content)
    try:
        cursor.execute(sql_update)
        db.commit()
        print('修改成功！')
    except:
        db.rollback()
        print('修改失败!')


def main():
    db = pymysql.connect(user='root', password='001122', host='localhost', port=3306, database='python',
                         charset="utf8")
    while True:
        print('《《《留言板》》》\n\n1、添加留言;\n2、删除留言;\n3、查询;\n4、修改;\n5、退出留言板。\n')
        flag = int(input('输入功能序号：'))
        if flag == 1:
            add(db)
        elif flag == 2:
            delete(db)
        elif flag == 3:
            display(db)
            search(db)
        elif flag == 4:
            update(db)
        elif flag == 5:
            break
        if int(input('\n是否继续？ 1/0：')) == 0:
            break
    db.close()


if __name__ == '__main__':
    main()
