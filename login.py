from App import app
from DBManager.DBHandler import dbHandler
from Entities.User import User
from Entities.BookingManager import booking_manager
import BookRoom
import displaybookings
import lrrs

from flask import render_template
from flask import request
from flask import jsonify
from flask import session
from datetime import datetime

import os

def login():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        return "You have already logged in.  Click <a href='/searchpage.html'>here</a> to search rooms."


@app.route('/checkuname',methods=['POST'])
def checkuname():

    # read the posted values from the UI
    uname = request.form['username']
    password = request.form['psw']

    oUser = User(uname)
    oUser.set_password(password)

    status = dbHandler.validate_user(oUser)

    if status == 1:
        session['uname'] = uname
        session['logged_in'] = True

    return jsonify({'success': status})
    

@app.route('/searchpage.html')
def searchpage():
    if session.get('logged_in'):
        return render_template("searchpage.html", mindate=datetime.today())
    else:
        return render_template("pleaseloginfirst.html")



@app.route("/")
def start():
    return login()


if __name__ == '__main__':
    print(datetime.today())
    app.secret_key = os.urandom(12)
    app.run()