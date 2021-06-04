#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:hello.py
# author:Asus
# datetime:2021/6/3 8:29
# software: PyCharm
'''
this is functiondescription
'''
# import module your need


from flask import Flask, render_template
from flask_bootstrap import Bootstrap

app = Flask(__name__)
bootstrap = Bootstrap(app)


@app.route('/')
def index():
    return render_template('index_bootstrap.html')


@app.route('/user')
def user():
    return render_template('user.html')


if __name__ == '__main__':
    app.run()

