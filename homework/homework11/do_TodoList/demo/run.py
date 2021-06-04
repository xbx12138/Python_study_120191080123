#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:views.py
# author:Asus
# datetime:2021/6/2 20:48
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

from flask import Flask, render_template

from model.model import todo_list as td

app = Flask('TodoList')


@app.route('/')
def index():
    context = td.getInfo()
    return render_template('base.html', contexts=context)


if __name__ == '__main__':
    app.run()
