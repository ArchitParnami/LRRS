import unittest
from flask import Flask,render_template,request
from datetime import datetime,timedelta
from App import app
from App import mysql


app = Flask(__name__)
class Test_DisplayMyBookings(unittest.TestCase):
    def test_displaymybooking(self):
        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.execute("call sp_displaybooking(%s)", ('archit'))
        cursor.fetchall()
        conn.commit()
        assert cursor.rowcount == 1

if __name__ == '__main__':
    unittest.main()