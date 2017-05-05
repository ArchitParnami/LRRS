import unittest
from login import checkuser

class Test_checkuser(unittest.TestCase):
 
    def setUp(self):
        pass
 
    def test_success1(self):
        self.assertEqual( checkuname('jma15',1234), {'success':1})
 
    def test_success2(self):
        self.assertEqual( checkuname('dshah27',1234), {'success':1})

    def test_success3(self):
        self.assertEqual( checkuname('aparnami',1234), {'success':1})

    def test_notsuccess1(self):
        self.assertEqual( checkuname('sd',342), {'success':0})

    def test_notsuccess2(self):
        self.assertEqual( checkuname('4','fd'), {'success':0})
 
 
if __name__ == '__main__':
    unittest.main()

