import unittest
from calculator import *

import unittest
from calculator import *

class TestCalculator(unittest.TestCase):

    # Partner 1
    def test_multiply(self):
        self.assertEqual(multiply(2, 2), 4)
        self.assertEqual(multiply(-2, 2), -4)
        self.assertEqual(multiply(-2, -2), 4)

    def test_divide(self):
        self.assertEqual(divide(10, 2), 5)
        self.assertEqual(divide(-10, 2), -5)
        self.assertEqual(divide(0, 5), 0)

    def test_log_invalid_argument(self):
        with self.assertRaises(ValueError):
            logarithm(2, -5)  # negative argument not allowed

    def test_hypotenuse(self):
        self.assertAlmostEqual(hypotenuse(3, 4), 5.0)
        self.assertAlmostEqual(hypotenuse(5, 12), 13.0)
        self.assertAlmostEqual(hypotenuse(0, 0), 0.0)

    def test_sqrt(self):
        self.assertAlmostEqual(square_root(16), 4.0)
        self.assertAlmostEqual(square_root(0), 0.0)
        with self.assertRaises(ValueError):
            square_root(-1)
