from flask import render_template,request,session
from datetime import datetime,timedelta
from App import app
from App import mysql
import lrrs

app.secret_key = 'abcd'
@app.route('/booking',methods=['POST'])
def redirecttobooking():
    _room = request.form['hdnID']
    session['hdnID'] = _room
    _startdate = session.get('startdate')
    _starttime = session.get('starttime')
    _starttimeformat = datetime.strptime(_starttime, "%I:%M %p")
    _starttimeformat = _starttimeformat.strftime("%H:%M:%S")
    if session.get('logged_in'):
        return render_template('booking.html',roomno=_room,date=_startdate,time=_starttimeformat)
    else:
        return render_template("pleaseloginfirst.html")

@app.route('/book',methods=['post'])
def book():
    _uname = session.get('uname')
    _room = session.get('hdnID')
    _startdate = session.get('startdate')
    _starttime =session.get('starttime')
    _name = request.form['bookingname']
    _starttimeformat  = datetime.strptime(_starttime, "%I:%M %p")
    _starttimeformat= _starttimeformat.strftime("%H:%M:%S")
    _endtimeformat = datetime.strptime(_starttime, "%I:%M %p") + timedelta(minutes=int(request.form['duration']))
    _endtimeformat = _endtimeformat.strftime("%H:%M:%S")
    conn = mysql.connect()
    cursor = conn.cursor()
    cursor.callproc('sp_booking', args=(_uname, _startdate, _name, _room, _starttimeformat, _endtimeformat))
    conn.commit()
    if session.get('logged_in'):
        return render_template('thankyou.html',roomno = _room)
    else:
        return render_template("pleaseloginfirst.html")