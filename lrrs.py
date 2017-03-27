from flask import render_template,request

from App import app
from App import mysql


# @app.route('/')
# def hello_world():
#     return render_template('searchpage.html')

@app.route('/search',methods=['POST'])
def search():

    _startdate = request.form['inputStartDate']
    _starttime = request.form['inputStartTime']
    _type = request.form['inputType']

    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_searchrooms', args=(_type, _starttime, _startdate))
    data = cursor.fetchall()
    return render_template('displayrooms.html', data=data)


