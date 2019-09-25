from flask import Flask, flash, redirect, escape, request, render_template, send_from_directory, session, abort
import sqlite3
from flask import g
from flask_login import LoginManager
import os

app = Flask(__name__)
login_manager = LoginManager(app)
login_manager.init_app(app)

app.secret_key = b'a932ik29ok3r02jker02323'


DATABASE = 'yogaz.db'

# DB config and functions

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

# main page

@app.route('/')
def indexpage():
    return render_template('index.html')

# login manager

@login_manager.user_loader
def load_user(user_id):
    return User.get(user_id)



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


@app.route('/result.html',methods = ['POST', 'GET'])
def result():
   if request.method == 'POST':
            result = request.form
            con = get_db()
            cur = con.cursor()
            cur.execute("INSERT INTO user (firstName, lastName, username, password, email, address, address2, country, state, zip) VALUES (?,?,?,?,?,?,?,?,?,?)", (result['firstName'],result['lastName'],result['username'],result['password'],result['email'],result['address'],result['address2'],result['country'],result['state'],result['zip']))
            con.commit()
            con.close()
            return render_template("result.html", result = result)
   else:
	    return render_template("index.html")

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

@app.route('/profile.html', methods=['GET', 'POST'])
def profile():
	   if request.method == 'POST':
           	result = request.form
           	con = get_db()
           	cur = con.cursor()
           	cur.execute("SELECT * FROM user WHERE username = ? and password = ? limit 1;", (result['username'],result['password']))
		userdata = cur.fetchall();
		if not userdata:
			flash('Authentication Error, please try again')
			session['logged_in'] = False
			return indexpage()
		else: 
			session['logged_in'] = True
			userId = str(userdata[0][0])
			cur.execute("SELECT classSchedule.datetime, classSchedule.description from classSchedule join booking on classSchedule.classScheduleId = booking.classScheduleId WHERE booking.userID = ?;", [userId])
			classesdata = cur.fetchall()
			session['userdata'] = userdata[0]
			session['classesdata'] = classesdata
          		return render_template('profile.html', userdata=userdata[0], classesdata=classesdata)
	   else:
		if session['logged_in']:
			return render_template('profile.html', userdata=session['userdata'], classesdata=session['classesdata'])
		else:
			return indexpage()


@app.route('/beginner.html')
def beginner():
        return render_template('beginner.html')

@app.route('/trainer.html')
def trainer():
   con = get_db()
   cur = con.cursor()
   cur.execute("SELECT * FROM trainer;")
   rows = cur.fetchall();
   return render_template('trainer.html', rows = rows)

@app.route('/classType.html')
def classType():
        return render_template('classType.html')

@app.route('/logout')
def logout():
    # remove the username from the session if it's there
    session.pop('userdata', None)
    session['logged_in'] = False
    return render_template('index.html')

if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(port=8888,debug=True)
