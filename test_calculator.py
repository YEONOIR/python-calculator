import unittest
from calculator import Calculator

class TestCalculator(unittest.TestCase):

    def setUp(self):
        self.calc = Calculator()

    def test_add(self):
        self.assertEqual(self.calc.add(1, 2), 3)
        self.assertEqual(self.calc.add(5, 2), 7)

    # Add the following test methods to the TestCalculator class:

    def test_sub(self):
        self.assertEqual(self.calc.subtract(2, -3), 5)
        self.assertEqual(self.calc.subtract(5, 3), 2)

    def test_mul(self):
        self.assertEqual(self.calc.multiply(2, 9), 18)
        self.assertEqual(self.calc.multiply(4, 3), 12)

    def test_div(self):
        self.assertEqual(self.calc.divide(10, 2), 5)
        self.assertEqual(self.calc.divide(10, 4), 2)

    def test_mod(self):
        self.assertEqual(self.calc.modulo(8, 2), 0)
        self.assertEqual(self.calc.modulo(12, 5), 2)

if __name__ == '__main__':
    unittest.main()