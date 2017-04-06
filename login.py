from LRRS.App import app
from LRRS.App import mysql

from flask import render_template
from flask import request
from flask import jsonify

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
    return render_template("login.html")


@app.route('/checkuser',methods = ['POST'])
def checkuname():
    # read the posted values from the UI
    uname = request.form['username']
    password = request.form['psw']
    return jsonify(checkuser(uname,password))
    

@app.route('/searchpage.html')
def searchpage():

    return render_template("searchpage.html")



@app.route("/")
def start():
    return login()


if __name__ == '__main__':
   app.run(debug = True)