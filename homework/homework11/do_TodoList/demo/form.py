#!/usr/bin/env python
# -*- coding:utf-8 -*-

# file:form.py
# author:Asus
# datetime:2021/6/5 12:26
# software: PyCharm
'''
this is functiondescription
'''
# import module your need

from flask_wtf import FlaskForm
from wtforms import StringField, SubmitField
from wtforms.validators import DataRequired


class Form(FlaskForm):
    content_add = StringField('Content', validators=[DataRequired()])
    # content_update = StringField('update', validators=[DataRequired()])
    submit = SubmitField('Add New Item')
