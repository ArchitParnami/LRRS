from flask import render_template, request, session, redirect, url_for
from datetime import datetime, timedelta
from LRRS.App import app
from LRRS.App import mysql
from LRRS.Entities.BookingManager import booking_manager
from LRRS.DBManager.ORM import ORM
from flask_login import login_required, current_user

@app.route('/booking', methods=['POST'])
@login_required
def redirect_to_booking():

    _room = request.form['hdnID']
    session['hdnID'] = _room
    _startdate = session.get('startdate')
    _starttime = session.get('starttime')
    _starttimeformat = datetime.strptime(_starttime, "%I:%M %p")
    _starttimeformat = _starttimeformat.strftime("%H:%M:%S")

    return render_template('booking.html', roomno=_room, date=_startdate, time=_starttimeformat)

@app.route('/book', methods=['post'])
@login_required
def book():
    _uname = current_user.username
    _room = session.get('hdnID')
    _startdate = session.get('startdate')
    _starttime = session.get('starttime')
    _name = request.form['bookingname']

    _startdate = ORM.string_to_date(_startdate)
    _starttimeformat = datetime.strptime(_starttime, "%I:%M %p")
    _endtimeformat = datetime.strptime(_starttime, "%I:%M %p") + timedelta(minutes=int(request.form['duration']))

    status, booking_id = booking_manager.try_book_room(_room, _startdate, _starttimeformat, _endtimeformat, _uname, _name)

    if status:
        return render_template('thankyou.html', roomno=_room)
    else:
        return render_template("Unavailable.html")

@app.route('/postBooking', methods=['post'])
@login_required
def after_book():
    button_clicked = request.form['hdnBtnId']
    if button_clicked == "btnHome":
        return redirect(url_for('searchpage'))
    if button_clicked == "btnBooking":
        return redirect(url_for('displaybooking'))
    if button_clicked == "btnLogout":
        return redirect('logout')