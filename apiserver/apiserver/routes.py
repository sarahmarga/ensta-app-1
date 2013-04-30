# -*- coding: utf-8 -*-
"""
Flaskr
~~~~~~

A microblog example application written as Flask tutorial with
Flask and sqlite3.

:copyright: (c) 2010 by Armin Ronacher.
:license: BSD, see LICENSE for more details.
"""
from __future__ import with_statement
from sqlite3 import dbapi2 as sqlite3
from flask import Flask, request, session, g, redirect, url_for, abort, \
     render_template, flash, _app_ctx_stack

# configuration
DATABASE = '/tmp/avisavi2.db'
DEBUG = True
SECRET_KEY = 'development key'



app = Flask(__name__)
app.config.from_object(__name__)
app.config.from_envvar('AVISAVI2_SETTINGS', silent=True)


def init_db():
    """Creates the database tables."""
    with app.app_context():
        db = get_db()
        with app.open_resource('schema3.sql') as f:
            db.cursor().executescript(f.read())
        db.commit()


def get_db():
    """Opens a new database connection if there is none yet for the
current application context.
"""
    top = _app_ctx_stack.top
    if not hasattr(top, 'sqlite_db'):
        sqlite_db = sqlite3.connect(app.config['DATABASE'])
        sqlite_db.row_factory = sqlite3.Row
        top.sqlite_db = sqlite_db

    return top.sqlite_db


@app.teardown_appcontext
def close_db_connection(exception):
    """Closes the database again at the end of the request."""
    top = _app_ctx_stack.top
    if hasattr(top, 'sqlite_db'):
        top.sqlite_db.close()



###### ROUTING ##########

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/personne')
def personne():
    db = get_db()
    cur = db.execute('select prenom, nom from personne order by id desc')
    entries = cur.fetchall()
    return render_template('personne.html',personne = personne)

@app.route('/personne', methods=['POST'])
def add_entry():
    db = get_db()
    db.execute('insert into personne (prenom, nom) values (?, ?)',
                 [request.form['ident1'], request.form['ident2']])
    db.commit()
    flash('New entry was successfully posted')
    return redirect(url_for('personne'))



@app.route('/fonction')
def fonction():
    return render_template('fonction.html')


if __name__ == '__main__':
    init_db()
    app.run()

