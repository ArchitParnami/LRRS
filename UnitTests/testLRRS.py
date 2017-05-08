import unittest
from App import app
from App import mysql


class TestLrrs(unittest.TestCase):
    def test_search(self):
        _startdate = '2017-03-23'
        _starttime = '01:00 PM'
        _type = 'G'

        conn = mysql.connect()
        cursor = conn.cursor()
        cursor.callproc('sp_searchrooms', args=(_type, _starttime, _startdate))
        assert cursor.rowcount == 1


if __name__ == '__main__':
    unittest.main()
