#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:model.py
# author:Asus
# datetime:2021/6/1 20:16
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


class todo_list(Base):
    # 第一个参数是数据表名，第二个参数是元数据，第三个参数表示自动加载
    __table__ = Table('todo_list', md, autoload=True)

    @classmethod
    def getInfo(cls):
        all_content = session.query(cls).all()
        todoList = []
        for content in all_content:
            todo = {'number': content.id, 'content': content.content}
            todoList.append(todo)
        return todoList


    @classmethod
    def add_todo(cls,content):
        try:
            session.add(todo_list(content=content, date=datetime.now()))
            session.commit()
        except Exception as e:
            session.rollback()
            print(e)
            return {'数据库异常，添加记录失败'}