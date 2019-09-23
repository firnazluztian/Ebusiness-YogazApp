from flask import Flask, escape, request, render_template, send_from_directory
import sqlite3
from flask import g
import os

app = Flask(__name__)

DATABASE = 'yogaz.db'

def get_db():
    db = getattr(g, '_database', None)
    if db is None:
        db = g._database = sqlite3.connect('yogaz.db')
    return db

def query_db(query, args=(), one=False):
    cur = get_db().execute(query, args)
    rv = cur.fetchall()
    cur.close()
    return (rv[0] if rv else None) if one else rv

@app.teardown_appcontext
def close_connection(exception):
    db = getattr(g, '_database', None)
    if db is not None:
        db.close()

app = Flask(__name__)

@app.route('/')
def indexpage():
    return render_template('index.html')


# Routes to static content

@app.route('/css/<path:path>')
def send_css(path):
        return send_from_directory('static/css', path)


@app.route('/js/<path:path>')
def send_js(path):
            return send_from_directory('static/js', path)


@app.route('/pic/<path:path>')
def send_pic(path):
            return send_from_directory('static/pic', path)


@app.route('/json/<path:path>')
def send_json(path):
            return send_from_directory('templates/json', path)


@app.route('/static/<path:path>')
def send_static(path):
                return send_from_directory('static/pic', path)


# Sub pages

@app.route('/signup.html')
def signup():
        return render_template('signup.html')


@app.route('/aboutUs.html')
def aboutUs():
        return render_template('aboutUs.html')

@app.route('/classSchedule.html')
def classSchedule():
   con = get_db()
   cur = con.cursor()
   cur.execute("select * from classSchedule;")

   rows = cur.fetchall();
   return render_template('classSchedule.html', rows = rows)

@app.route('/contactUs.html')
def contactUs():
        return render_template('contactUs.html')


@app.route('/index.html')
def indexPage():
        return render_template('index.html')

@app.route('/profile.html')
def profile():
        return render_template('profile.html')


@app.route('/beginner.html')
def beginner():
        return render_template('beginner.html')

@app.route('/trainer.html')
def trainer():
   con = get_db()
   cur = con.cursor()
   cur.execute("select * from trainer;")
   rows = cur.fetchall();
   return render_template('trainer.html', rows = rows)

@app.route('/classType.html')
def classType():
        return render_template('classType.html')


