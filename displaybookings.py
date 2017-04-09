from flask import render_template,request,session
from LRRS.App import app
from LRRS.App import mysql
from LRRS.Entities.BookingManager import booking_manager

@app.route('/displaybookings',methods=['POST'])
def displaybooking():

    _uname = session.get('uname')
    bookings = booking_manager.get_user_bookings(_uname)
    #bookings = bookings.sort(key=lambda booking: booking.start_date, reverse=True)

    if session.get('logged_in'):
        return render_template('displaymybooking.html',user_bookings=bookings)
    else:
        return render_template("pleaseloginfirst.html")