import unittest
from unittest import TestCase

from PythonLanguage.unittest import calc


class TestCalc(TestCase):
    def test_add(self):
        self.assertEqual(calc.add(7, 3), 10)
        self.assertEqual(calc.add(100, 33), 133)
        self.assertEqual(calc.add(-17, 117), 100)

    def test_subtract(self):
        self.assertEqual(0, calc.subtract(1, 1))
        self.assertEqual(-2, calc.subtract(-1, 1))
        self.assertEqual(0, calc.subtract(-1, -1))

    def test_multiply(self):
        self.assertEqual(2, calc.multiply(1, 2))
        self.assertEqual(-1, calc.multiply(-1, 1))
        self.assertEqual(1, calc.multiply(-1, -1))

    def test_divide(self):
        self.assertEqual(0.5, calc.divide(1, 2))
        self.assertEqual(2, calc.divide(4, 2))
        self.assertEqual(2, calc.divide(-4, -2))

    def test_divide_by_zero(self):
        self.assertRaises(ValueError, calc.divide, 1, 0)
        self.assertRaises(ValueError, calc.divide, 0, 0)
        # or
        with self.assertRaises(ValueError):
            calc.divide(1, 0)


if __name__ == '__main__':
    unittest.main()
