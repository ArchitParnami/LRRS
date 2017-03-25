import unittest
from login import queryuser
 
class Test_queryuser(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_correctuser1(self):
        self.assertEqual( queryuser('jma15',1234), (('jma15','1234'),))
 
    def test_correctuser2(self):
        self.assertEqual( queryuser('dshah27',1234), (('dshah27','1234'),))

    def test_correctuser3(self):
        self.assertEqual( queryuser('aparnami',1234), (('aparnami','1234'),))

    def test_wronguser1(self):
        self.assertEqual( queryuser('sd',342), ())

    def test_wronguser2(self):
        self.assertEqual( queryuser('4','fd'), ())
 
 
if __name__ == '__main__':
    unittest.main()