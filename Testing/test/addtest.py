import unittest
from service.add import add


class AddTest(unittest.TestCase):
    def testadd1(self):
        self.assertEqual(add(0, 0), 0)

    def testadd2(self):
        self.assertEqual(add(-1, 1), 0)

    def testadd3(self):
        self.assertEqual(add(-1, 3), 2)

    def testadd4(self):
        self.assertEqual(add("A", 3), None)
