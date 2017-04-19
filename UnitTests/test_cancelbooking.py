import unittest
from DBManager.DBHandler import dbHandler
from flask import Flask

app = Flask(__name__)

class Test_Cancelbooking(unittest.TestCase):
    def test_cancelbooking(self):
        _bookingid = '1'
        assert dbHandler.cancel_booking(_bookingid) == 1


if __name__ == '__main__':
    unittest.main()