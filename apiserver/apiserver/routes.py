#!/usr/bin/python
# -*- coding: utf-8 -*- 
from flask import render_template,Markup,request,flash,redirect
from flask.views import MethodView

from apiserver import app

###### ROUTING ##########

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/apropos')
def apropos():
    return render_template('apropos.html')
