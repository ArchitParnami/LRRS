from flask import render_template,request,session
from App import app
from App import mysql
from Entities.BookingManager import booking_manager
from datetime import datetime, timedelta
from DBManager.DBHandler import dbHandler

@app.route('/displaybookings',methods=['POST'])
def displaybooking():
    _starttime = datetime.now().time()
    currenttime = _starttime.strftime("%H:%M:%S")
    _startdate = datetime.now().date()
    _uname = session.get('uname')
    bookings = booking_manager.get_user_bookings(_uname)
    #bookings = bookings.sort(key=lambda booking: booking.start_date, reverse=True)

    if session.get('logged_in'):
        return render_template('displaymybooking.html',user_bookings=bookings,currenttime=datetime.strptime(currenttime,"%H:%M:%S").time(),startdate=_startdate)
    else:
        return render_template("pleaseloginfirst.html")


@app.route('/cancel',methods=['POST'])
def cancelbooking():
    _uname = session.get('uname')
    _bookingid = request.form['hdnBookingid']
    dbHandler.cancel_booking(_bookingid)
    _starttime = datetime.now().time()
    currenttime = _starttime.strftime("%H:%M:%S")
    _startdate = datetime.now().date()
    _uname = session.get('uname')
    bookings = booking_manager.get_user_bookings(_uname)
    # bookings = bookings.sort(key=lambda booking: booking.start_date, reverse=True)

    if session.get('logged_in'):
        return render_template('displaymybooking.html', user_bookings=bookings,currenttime=datetime.strptime(currenttime, "%H:%M:%S").time(), startdate=_startdate)
    else:
        return render_template("pleaseloginfirst.html")

@app.route('/notify',methods=['POST'])
def notify():
    _uname = session.get('uname')
    _bookingid = request.form['hdnBookingid']
    dbHandler.notify_booking(_bookingid)
    _starttime = datetime.now().time()
    currenttime = _starttime.strftime("%H:%M:%S")
    _startdate = datetime.now().date()
    _uname = session.get('uname')
    bookings = booking_manager.get_user_bookings(_uname)
    # bookings = bookings.sort(key=lambda booking: booking.start_date, reverse=True)

    if session.get('logged_in'):
        return render_template('displaymybooking.html', user_bookings=bookings,currenttime=datetime.strptime(currenttime, "%H:%M:%S").time(), startdate=_startdate)
    else:
        return render_template("pleaseloginfirst.html")

