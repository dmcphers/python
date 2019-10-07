import unittest
import math
import random


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
    to_float = None
    bitlength_fun = None
    type_fun = None
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

    # Floor function
    def floorfun(self, x):
        self.x = x
        self.floor_fun = math.floor(x)
        return self.floor_fun

    # Max function
    def maxfun(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.max_fun = max(x, y, z)
        return self.max_fun

    # Min function
    def minfun(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.min_fun = min(x, y, z)
        return self.min_fun

    # Pow function
    def powfun(self, x, y):
        self.x = x
        self.y = y
        self.pow_fun = pow(x, y)
        return self.pow_fun

    # Round function
    def roundfun(self, x, y):
        self.x = x
        self.y = y
        self.round_fun = round(x, y)
        return self.round_fun

    # Square root function
    def sqrtfun(self, x):
        self.x = x
        self.sqrt_fun = math.sqrt(x)
        return self.sqrt_fun

    # Random range function
    def randrangefun(self, x, y, z):
        self.x = x
        self.y = y
        self.z = z
        self.randrange_fun = random.randrange(x, y, z)
        return self.randrange_fun

    # Random function
    def randomfun(self):
        self.random_fun = random.random()
        return self.random_fun

    # int() function for coercing to type int
    def intfun(self, x):
        self.to_int = int(x)
        return self.to_int

    # float() function for coercing to type float
    def floatfun(self, x):
        self.to_float = float(x)
        return self.to_float

    # bit_length() function for finding number of bits required to represent an integer
    def bitlengthfun(self, x):
        self.x = x
        self.bitlength_fun = x.bit_length()
        return self.bitlength_fun

    # type() function for displaying type of object
    def typefun(self, x):
        self.x = x
        self.type_fun = type(x)
        return self.type_fun


class TestNumericFunctions(unittest.TestCase):

    def setUp(self):
        self.numfun = NumericFunctions()

    def test_ceil_neg(self):
        self.assertEqual(self.numfun.ceilfun(-34.23), -34)

    def test_abs_neg(self):
        self.assertEqual(self.numfun.absfun(-34), 34)

    def test_floor_neg(self):
        self.assertEqual(self.numfun.floorfun(-34.23), -35)

    def test_max_neg(self):
        self.assertEqual(self.numfun.maxfun(-34, -24, -14), -14)

    def test_min_neg(self):
        self.assertEqual(self.numfun.minfun(-34, -24, -14), -34)

    def test_pow_neg(self):
        self.assertEqual(self.numfun.powfun(-3, 2), 9)

    def test_round_neg(self):
        self.assertEqual(self.numfun.roundfun(-3.445, 2), -3.44)

    def test_sqrt(self):
        self.assertEqual(self.numfun.sqrtfun(25), 5)

    def test_randrange(self):
        print(self.numfun.randrangefun(0, 100, 1))

    def test_random(self):
        print(self.numfun.randomfun())

    def test_intfun(self):
        self.assertEqual(self.numfun.intfun(23.8), 23)

    def test_floatfun(self):
        self.assertEqual(self.numfun.floatfun(23), 23.0)

    def test_bitlengthfun(self):
        self.assertEqual(self.numfun.bitlengthfun(7), 3)

    def test_type(self):
        print(self.numfun.typefun('Hello'))


if __name__ == '__main__':
    unittest.main()
