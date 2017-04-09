from flask import render_template, request, session
from datetime import datetime, timedelta
from LRRS.App import app
from LRRS.App import mysql
from LRRS.Entities.BookingManager import booking_manager


@app.route('/booking', methods=['POST'])
def redirect_to_booking():

    _room = request.form['hdnID']
    session['hdnID'] = _room
    _startdate = session.get('startdate')
    _starttime = session.get('starttime')
    _starttimeformat = datetime.strptime(_starttime, "%I:%M %p")
    _starttimeformat = _starttimeformat.strftime("%H:%M:%S")

    if session.get('logged_in'):
        return render_template('booking.html', roomno=_room, date=_startdate, time=_starttimeformat)
    else:
        return render_template("pleaseloginfirst.html")


@app.route('/book', methods=['post'])
def book():

    _uname = session.get('uname')
    _room = session.get('hdnID')
    _startdate = session.get('startdate')
    _starttime = session.get('starttime')
    _name = request.form['bookingname']

    _starttimeformat = datetime.strptime(_starttime, "%I:%M %p")
    _endtimeformat = datetime.strptime(_starttime, "%I:%M %p") + timedelta(minutes=int(request.form['duration']))

    if session.get('logged_in'):

        status = booking_manager.try_book_room(_room, _startdate, _starttimeformat, _endtimeformat, _uname, _name)

        if status:
            return render_template('thankyou.html', roomno=_room)
        else:
            return "Room unavailable in this duration. Please try again later"

    else:
        return render_template("pleaseloginfirst.html")
