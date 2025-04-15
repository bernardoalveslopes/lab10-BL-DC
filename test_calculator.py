import unittest
from calculator import *
#https://github.com/bernardoalveslopes/lab10-BL-DC
# Partner 1: Bernardo Lopes
# Partner 2: Darryl Culver

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(sub(10, 4), 6)
        self.assertEqual(sub(0, 5), -5)
        self.assertEqual(sub(-3, -3), 0)

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(log(2, 8), 3.0)
        self.assertAlmostEqual(log(10, 1000), 3.0)
        self.assertAlmostEqual(log(math.e, math.e**2), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            log(1, 10)  # base cannot be 1

