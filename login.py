from flask import Flask, redirect, url_for, request,json
#render_template is for render html to your server
from flask import render_template, jsonify
from flask import session
import os
# sql connector
from flaskext.mysql import MySQL


app = Flask(__name__)

# # MySQL configurations
# mysql = MySQL()
# app.config['MYSQL_DATABASE_USER'] = 'root'
# app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
# app.config['MYSQL_DATABASE_DB'] = 'lrrs'
# app.config['MYSQL_DATABASE_HOST'] = 'localhost'
# mysql.init_app(app)


mysql = MySQL()
app.config['MYSQL_DATABASE_USER'] = 'root'
app.config['MYSQL_DATABASE_PASSWORD'] = '1234'
app.config['MYSQL_DATABASE_DB'] = 'lrrs'
app.config['MYSQL_DATABASE_HOST'] = 'localhost'
mysql.init_app(app)

def queryuser(username,password):
    conn = mysql.connect()
    cursor = conn.cursor()
    query_str = "SELECT * FROM user_pw WHERE username='%s' AND password='%s';"%(username, password)
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

@app.route('/')
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
    if checkuser(uname,password)=={'success':1}:
        print('assert true1')
        session['logged_in'] = True
        session[uname]=password
        print('assert true2')
    return jsonify(checkuser(uname,password))
    

@app.route('/searchpage.html')
def searchpage():
    # if session.get('logged_in'):
    if session.get('logged_in'):
        return render_template("searchpage.html")
    else:
        return render_template("pleaseloginfirst.html")
    

if __name__ == '__main__':
   app.secret_key = os.urandom(12)
   app.run(debug = True)
