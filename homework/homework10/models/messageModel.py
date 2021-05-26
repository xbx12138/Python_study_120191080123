#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:messageModel.py
# author:Asus
# datetime:2021/5/25 19:18
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

from datetime import datetime
from . import session
from sqlalchemy import MetaData, Table
from sqlalchemy.ext.declarative import declarative_base
from . import engine

Base = declarative_base()
metadata = Base.metadata
md = MetaData(bind=engine)


class MessageModel(Base):
    # 第一个参数是数据表名，第二个参数是元数据，第三个参数表示自动加载
    __table__ = Table('message_board', md, autoload=True)

    @classmethod
    def get_all_content(cls, **kwargs):
        query_content = session.query(cls)
        all_content = query_content.all()
        for content in all_content:
            if content.exist == 1:
                print(content.Message_content, end=' ————')
                print(content.author, end=' ')
                print(content.Message_time)

    @classmethod
    def add_content(cls, **kwargs):
        Message_content = input('输入留言内容：')
        author = input('输入你的姓名：')
        try:
            session.add(MessageModel(Message_content=Message_content, author=author, Message_time=datetime.now(), exist=1))
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)
            return {'数据库异常，添加记录失败'}

    @classmethod
    def del_content(cls, **kwargs):
        query_content = session.query(cls)
        try:
            content = query_content.filter(MessageModel.Message_content == input('\n输入需删除的留言内容:'))
            print(content[0].Message_content, end=' ————')
            print(content[0].author, end=' ')
            print(content[0].Message_time)
            if input('\n是否删除？ 1/0：') != 0:
                content[0].exist = 0
                session.commit()
        except Exception as e:
            session.rollback()
            print(e)
            return {'数据库异常，删除记录失败'}

    @classmethod
    def search_content(cls, **kwargs):
        query_content = session.query(cls)
        try:
            all_content = query_content.filter(MessageModel.author == input('输入查询的留言人：'))
            for content in all_content:
                if content.exist == 1:
                    print(content.Message_content, end=' ————')
                    print(content.author, end=' ')
                    print(content.Message_time)
        except Exception as e:
            session.rollback()
            print(e)
            return {'数据库异常'}

    @classmethod
    def update_content(cls, **kwargs):
        query_content = session.query(cls)
        try:
            content = query_content.filter(MessageModel.Message_content == input('\n输入需修改的留言:'))
            print(content[0].Message_content, end=' ————')
            print(content[0].author, end=' ')
            print(content[0].Message_time)
            if input('\n是否修改？ 1/0：') != 0:
                content[0].Message_content = input('\n输入修改后的留言：')
                session.commit()
        except Exception as e:
            session.rollback()
            print(e)
            return {'数据库异常，删除记录失败'}
