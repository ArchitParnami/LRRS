import unittest
from login import checkuser

class Test_checkuser(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_success1(self):
        self.assertEqual( checkuser('jma15',1234), {'success':0})
 
    def test_success2(self):
        self.assertEqual( checkuser('dshah27', 'abcd'), {'success':1})

    def test_success3(self):
        self.assertEqual( checkuser('aparnami',1234), {'success':0})

    def test_notsuccess1(self):
        self.assertEqual( checkuser('sd',342), {'success':0})

    def test_notsuccess2(self):
        self.assertEqual( checkuser('4','fd'), {'success':0})
 
 
if __name__ == '__main__':
    unittest.main()

