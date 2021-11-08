import unittest
from service.great import large

class greatTest(unittest.TestCase):
    def testGreat1(self):
        self.assertEqual(large(3,4,5),5)
    def testGreat2(self):
        self.assertEqual(large(9,5,7),9)
    def testGreat3(self):
        self.assertEqual(large(3,55,8),55)
    def testGreat4(self):
        self.assertEqual(large(30,55.5,0),55.5)
    def testGreat5(self):
        self.assertEqual(large(-1,-2,-0.5), -0.5)
    def testGreat6(self):
        self.assertEqual(large("A","B",5), "Error")





