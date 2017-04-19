import unittest
from DBManager.DBHandler import dbHandler
from flask import Flask

app = Flask(__name__)

class Test_Notify(unittest.TestCase):
    def test_notify(self):
        _bookingid = '10'
        assert dbHandler.notify_booking(_bookingid) == 1



if __name__ == '__main__':
    unittest.main()