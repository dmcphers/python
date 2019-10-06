import unittest
import math


# Class to handle numeric functions
class NumericFunctions:

    ceil_fun = None
    abs_fun = None
    floor_fun = None
    max_fun = None
    min_fun = None
    pow_fun = None
    round_fun = None
    sqrt_fun = None
    randrange_fun = None
    random_fun = None
    to_int = None
    to_long = None
    to_float = None
    x = None
    y = None
    z = None

    def __init__(self):
        pass

    # Ceil function
    def ceilfun(self, x):
        self.x = x
        self.ceil_fun = math.ceil(x)
        return self.ceil_fun

    # Abs function
    def absfun(self, x):
        self.x = x
        self.abs_fun = abs(x)
        return self.abs_fun


class TestNumericFunctions(unittest.TestCase):

    def setUp(self):
        self.numfun = NumericFunctions()

    def test_ceil_neg(self):
        self.assertEqual(self.numfun.ceilfun(-34.23), -34)

    def test_abs_neg(self):
        self.assertEqual(self.numfun.absfun(-34), 34)


if __name__ == '__main__':
    unittest.main()
