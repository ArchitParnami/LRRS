import unittest
from flask.ext.mysql import MySQL
from flask import Flask,render_template,request
from datetime import datetime,timedelta
from App import app
from App import mysql


app = Flask(__name__)

class Testbooking(unittest.TestCase):
    def test_booking(self):
        _room = 'G102'
        _startdate = '2017-04-05'
        _starttime = '10:30 AM'
        _name = 'testbooking'
        _starttimeformat = datetime.strptime(_starttime, "%I:%M %p")
        _starttimeformat = _starttimeformat.strftime("%H:%M:%S")
        _endtimeformat = datetime.strptime(_starttime, "%I:%M %p") + timedelta(minutes=int(30))
        _endtimeformat = _endtimeformat.strftime("%H:%M:%S")
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_booking', args=('dshah27', _startdate, _name, _room, _starttimeformat, _endtimeformat))
        conn.commit()
        assert cursor.rowcount == 1


if __name__ == '__main__':
    unittest.main()


