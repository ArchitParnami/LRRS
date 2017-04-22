from flask import render_template,request, session
from datetime import datetime

from LRRS.App import app
from LRRS.App import mysql
from LRRS.DBManager.ORM import ORM
from LRRS.Entities.BookingManager import booking_manager

@app.route('/search',methods=['POST'])
def search():

    start_date = request.form['inputStartDate']
    start_time = request.form['inputStartTime']
    room_type = request.form['inputType']

    session['startdate'] = start_date
    session['starttime'] = start_time

    room_type = ORM.room_type_to_enum[room_type]
    st = datetime.strptime(start_time, "%I:%M %p")
    start_date = ORM.string_to_date(start_date)

    avail = booking_manager.search(start_date, st, room_type)

    data=[]
    for room, st, et in avail:
        data.append([room.id, room.room_number, room.capacity, room.location.value, st.time(), et.time()])

    if session.get('logged_in'):

        return render_template('displayrooms.html', data=data, search_date=start_date.date(),
                               search_time=start_time, room_type=room_type.value)
    else:

        return render_template("pleaseloginfirst.html")
