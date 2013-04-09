#!/usr/bin/python
#This file creates a Python package
from flask import Flask
app = Flask('apiserver')
app.secret_key = 'some_secret_random'

import apiserver.routes

