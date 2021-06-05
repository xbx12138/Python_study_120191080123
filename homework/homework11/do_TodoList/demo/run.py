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
from form import Form
from model.model import todo_list as td

app = Flask('TodoList')
app.config['SECRET_KEY'] = '80fff76642694e618c85808b89062c7e'


@app.route('/', methods=['GET', 'POST'])
def index():
    context = td.getInfo()
    form = Form()
    if form.validate_on_submit():
        content_add = form.content_add.data
        if content_add != None:
            print(content_add)
            td.add_todo(content_add)
    else:
        print('提交表单失败！')
    return render_template('base.html', contexts=context, form=form)


if __name__ == '__main__':
    app.run()
