#https://github.com/bernardoalveslopes/lab10-BL-DC
import unittest
from calculator import *

# Partner 1: Bernardo Lopes
# Partner 2: Darryl Culver

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

# partner 2
    def test_add(self):
        self.assertEqual(add(2, 3), 5)
        self.assertEqual(add(-1, 1), 0)
        self.assertEqual(add(0, 0), 0)

    def test_subtract(self):
        self.assertEqual(subtract(10, 4), 6)
        self.assertEqual(subtract(0, 5), -5)
        self.assertEqual(subtract(-3, -3), 0)


# partner 1
    def test_multiply(self):
        self.assertEqual(mul(4,4),16)
        self.assertEqual(mul(-2,2),4)
        self.assertEqual(mul(-10,-2),20)

    def test_divide(self):
        self.assertEqual(div(8,2), 4)
        self.assertEqual(div(10,-2), -5)
        self.assertEqual(div(-20,-2), -10)


## Partner 2

    def test_divide_by_zero(self):
        with self.assertRaises(ZeroDivisionError):
            div(5, 0)

    def test_logarithm(self):
        self.assertAlmostEqual(logarithm(2, 8), 3.0)
        self.assertAlmostEqual(logarithm(10, 1000), 3.0)
        self.assertAlmostEqual(logarithm(math.e, math.e**2), 2.0)

    def test_log_invalid_base(self):
        with self.assertRaises(ValueError):
            logarithm(1, 10)  # base cannot be 1


## Partner 1

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(5, 0)

    det

