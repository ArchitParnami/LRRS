from LRRS.App import app
from LRRS.DBManager.DBHandler import dbHandler
from LRRS.Entities.User import User
from LRRS.Entities.BookingManager import booking_manager

from LRRS import lrrs
from LRRS import BookRoom
from LRRS import displaybookings

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
def login():
    if current_user.is_authenticated:
        return redirect(url_for('searchpage'))
    else:
        return render_template("login.html")

@app.route("/logout")
@login_required
def logout():
    logout_user()
    return redirect(url_for('login'))

@app.route('/checkuname',methods=['POST'])
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
@login_required
def searchpage():
    return render_template("searchpage.html", mindate=datetime.today())


@app.route("/")
def start():
    if current_user.is_authenticated:
        return redirect(url_for('searchpage'))
    else:
        return redirect(url_for('login'))


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run(debug=True, threaded=True)