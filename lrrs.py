from flask import Flask,render_template,request
import json
import ctypes
from flask import session
from flaskext.mysql import MySQL
from flask import url_for, redirect

app = Flask(__name__)


@app.route('/')
def hello_world():
    return render_template('searchpage.html')

@app.route('/search',methods=['POST'])
def search():

    _starttime = request.form['inputStartTime']
    _type = request.form['inputType']
    mysql = MySQL()
    # MySQL configurations
    app.config['MYSQL_DATABASE_USER'] = 'root'
    app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
    app.config['MYSQL_DATABASE_DB'] = 'lrrs'
    app.config['MYSQL_DATABASE_HOST'] = 'localhost'
    mysql.init_app(app)

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_searchrooms', args=(_type, _starttime))
    data = cursor.fetchall()
    return render_template('displayrooms.html', data=data)



if __name__ == '__main__':
    app.run()
