from flask import Flask, redirect, url_for, request,json,session
#render_template is for render html to your server
import lrrs
import datetime
from flask import render_template, jsonify
import os
# sql connector

from App import  mysql
from App import  app


def queryuser(username,password):
    conn = mysql.connect()
    cursor = conn.cursor()
    query_str = "SELECT * FROM user_info WHERE uname='%s' AND password='%s';"%(username, password)
    cursor.execute(query_str)
    return_data = cursor.fetchall()
    cursor.close()
    conn.close()
    return return_data

def checkuser(_uname,_password):

    print(_uname)
    print(_password)

    res_data = queryuser(_uname,_password)
    
    print('return type is list')
    print(res_data)
    # return json.dumps({res_data[0][0]:res_data[0][1]})
    if len(res_data)==0 or res_data is None:
        print ('not found')
        status = {'success':0}
    else:
        print( 'found')
        status = {'success':1}
    return status

def login():
    if not session.get('logged_in'):
        return render_template("login.html")
    else:
        return "You have already logged in.  Click <a href='/searchpage.html'>here</a> to search rooms."


@app.route('/checkuname.xyz',methods = ['POST'])
def checkuname():
    # read the posted values from the UI

    uname = request.form['username']
    password = request.form['psw']
    if checkuser(uname, password) == {'success': 1}:
        session['uname'] = uname
        session['logged_in'] = True
        password = request.form['psw']
    return jsonify(checkuser(uname,password))
    

@app.route('/searchpage.html')
def searchpage():
    # if session.get('logged_in'):
    if session.get('logged_in'):
        return render_template("searchpage.html",mindate=datetime.date.today())
    else:
        return render_template("pleaseloginfirst.html")

@app.route("/")
def start():
    return login()


if __name__ == '__main__':
    app.secret_key = os.urandom(12)
    app.run()