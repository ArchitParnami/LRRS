from App import app
from DBManager.DBHandler import dbHandler
#from LRRS.DBManager.MockDBHandler import dbHandler

from Entities.User import User
from Entities.BookingManager import booking_manager

import lrrs
import BookRoom
import displaybookings
from nocache import nocache

from flask import render_template, redirect, url_for
from flask import request
from flask import jsonify
from flask import session
from flask_login import LoginManager, login_required, login_user, logout_user, current_user
from datetime import datetime

import os

loginManager = LoginManager()
loginManager.init_app(app)
loginManager.login_view="login"

@loginManager.user_loader
def load_user(user_id):
    return dbHandler.get_user(user_id)

@app.route('/login')
@nocache
def login():
    if current_user.is_authenticated:
        return redirect(url_for('searchpage'))
    else:
        return render_template("login.html")

@app.route("/logout")
@nocache
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/checkuname',methods=['POST'])
@nocache
def checkuname():

    uname = request.form['username']
    password = request.form['psw']

    oUser = User(uname)
    oUser.set_password(password)

    status = dbHandler.validate_user(oUser)

    if status == 1:
        oUser.authenticate()
        login_user(oUser)

    return jsonify({'success': status})
    

@app.route('/searchpage.html')
@app.route('/search')
@app.route('/booking')
@nocache
@login_required
def searchpage():
    return render_template("searchpage.html", mindate=datetime.today())


@app.route("/")
@nocache
def start():
    if current_user.is_authenticated:
        return redirect(url_for('searchpage'))
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, threaded=True)