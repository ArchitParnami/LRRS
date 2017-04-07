import unittest
from flask.ext.mysql import MySQL
from flask import Flask,render_template,request

app = Flask(__name__)
class TestLrrs(unittest.TestCase):
    def test_search(self):
        _startdate = '2017-03-23'
        _starttime = '01:00 PM'
        _type = 'G'
        mysql = MySQL()
        # MySQL configurations
        app.config['MYSQL_DATABASE_USER'] = 'root'
        app.config['MYSQL_DATABASE_PASSWORD'] = 'root'
        app.config['MYSQL_DATABASE_DB'] = 'lrrs'
        app.config['MYSQL_DATABASE_HOST'] = 'localhost'
        mysql.init_app(app)

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_searchrooms', args=(_type, _starttime, _startdate))
        assert cursor.rowcount == 1

if __name__ == '__main__':
    unittest.main()

