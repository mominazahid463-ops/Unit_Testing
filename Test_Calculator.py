import unittest
from calculator import Calculator

class Test_Calculator(unittest.TestCase):

    def setUp(self):
        self.cal = Calculator()
    def tearDown(self):
        del self.cal

    def test_Add_positiveValues(self):
        self.assertEqual(self.cal.Add(2,3), 5)

    def test_Subtract_positiveValues(self):
        self.assertEqual(self.cal.Subtract(3,2), 1)

    def test_Multiply_positiveValues(self):
        self.assertEqual(self.cal.Multiply(2,3), 6)

    def test_DividePositiveValues(self):
        self.assertEqual(self.cal.Divide(4,2), 2)