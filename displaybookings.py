from flask import render_template,request,session, redirect, url_for
from LRRS.App import app
from LRRS.App import mysql
from LRRS.Entities.BookingManager import booking_manager
from datetime import  datetime, timedelta
from LRRS.DBManager.ORM import ORM
from flask_login import login_required, current_user

@app.route('/displaybookings',methods=['GET'])
@login_required
def displaybooking():

    current_time = datetime.now().time()
    current_time = ORM.time_to_string(current_time)
    current_time = ORM.string_to_time(current_time).time()
    current_date = datetime.now().date()

    _uname = current_user.username
    bookings = booking_manager.get_user_bookings(_uname)
    bookings.sort(key=lambda booking: (booking.start_date, booking.start_time), reverse=True)


    return render_template('displaymybooking.html', user_bookings=bookings,
                               currenttime=current_time, currentdate=current_date, timedelta=timedelta)

@app.route('/modifybooking', methods=['POST'])
def modify_booking():
    booking_id = request.form['hdnBookingid']
    request_type = request.form['hdnRequestType']

    message = ""

    if request_type == "cancel":
        booking_manager.cancel_booking(booking_id)
        message = "Your booking has been cancelled"

    elif request_type == "checkin":
        booking_manager.check_in(booking_id)
        message = "Your booking has started"

    elif request_type == "end":
        booking_manager.end_booking(booking_id)
        message = "Your booking has completed"

    else:
        message = "Invalid request"

    return redirect(url_for('displaybooking'))

@app.route('/fromBooking', methods=['POST'])
def from_bookings():
    button_clicked = request.form['hdnBtnId']
    if button_clicked == "btnHome":
        return redirect(url_for('searchpage'))
    if button_clicked == "btnLogout":
        return redirect(url_for('logout'))