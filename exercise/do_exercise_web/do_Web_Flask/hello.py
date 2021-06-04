#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:hello.py
# author:Asus
# datetime:2021/6/1 16:11
# software: PyCharm
'''
this is functiondescription
'''
# import module your need


from flask import Flask
from flask import request

app = Flask(__name__)


@app.route('/', methods=['GET', 'POST'])
def home():
    return '<h1> 付冲 变傻子 </h1>'


@app.route('/signin', methods=['GET'])
def signin_form():
    return '''<form action="/signin" method="post">
                 <p><input name="username"></p>
                 <p><input name="password" type="password"></p>
                 <p><button type="submit">Sign In</button></p>
                 </form>'''


@app.route('/signin', methods=['POST'])
def signin():
    if request.form['username'] == 'admin' and request.form['password'] == 'password':
        return '<h3>Hello, admin!</h3>'
    return '<h3>Bad username or password.</h3>'


if __name__ == '__main__':
    app.run()