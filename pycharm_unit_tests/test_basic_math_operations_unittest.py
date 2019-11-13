import unittest


# Class to handle basic arithmetic operations
class BasicMathOperations:

	sum = None
	product = None
	quotient = None
	difference = None
	x = None
	y = None

	def __init__(self):
		pass

	# Add method
	def add(self, x, y):
		if x is None or y is None:
			return self.sum
		else:
			self.x = x
			self.y = y
			self.sum = self.x + self.y
		return self.sum

# 	# Multiply method
	def multiply(self, x, y):
		self.x = x
		self.y = y
		self.product = self.x * self.y
		return self.product

# 	# Divide function
	def divide(self, x, y):
		self.x = x
		self.y = y
		self.quotient = self.x / self.y
		return self.quotient

# 	# Subtract function
	def subtract(self, x, y):
		self.x = x
		self.y = y
		self.difference = self.x - self.y
		return self.difference


class TestBasicMathOperations(unittest.TestCase):
	def setUp(self):
		self.bmo = BasicMathOperations()

	def test_add_pos(self):
		self.assertEqual(self.bmo.add(3, 4), 7)

	def test_add_neg(self):
		self.assertEqual(self.bmo.add(-3, -4), -7)

	def test_add_pos_neg(self):
		self.assertEqual(self.bmo.add(-3, 4), 1)

	def test_add_zero(self):
		self.assertEqual(self.bmo.add(0, 4), 4)

	def test_add_null(self):
		self.assertEqual(self.bmo.add(3, None), None)

	# method fails because 2 values are required per the class definition
	# def test_add_value_missing(self):
	# 	self.assertEqual(self.bmo.add(3,), 3)

	# method fails because 2 values are required per the class definition
	# def test_add_none(self):
	# 	self.assertEqual(self.bmo.add(), )

	def test_add_large_pos_nums(self):
		self.assertEqual(self.bmo.add(4738494329, 7529383821), 12267878150)

	def test_add_large_neg_nums(self):
		self.assertEqual(self.bmo.add(-4738494329, -7529383821), -12267878150)

	def test_subtract_pos(self):
		self.assertEqual(self.bmo.subtract(4, 3), 1)

	def test_subtract_neg(self):
		self.assertEqual(self.bmo.subtract(-4, -3), -1)

	def test_subtract_pos_neg(self):
		self.assertEqual(self.bmo.subtract(-4, 3), -7)

	def test_subtract_zero(self):
		self.assertEqual(self.bmo.subtract(0, 3), -3)
		self.assertEqual(self.bmo.subtract(3, 0), 3)

	# method fails because 2 values are required per the class definition
	# def test_subtract_value_missing(self):
	# 	self.assertEqual(self.bmo.subtract(4), 4)

	# method fails because 2 values are required per the class definition
	# def test_subtract_none(self):
	# 	self.assertEqual(self.bmo.subtract(), )

	def test_subtract_pos_largenums(self):
		self.assertEqual(self.bmo.subtract(7529383821, 4738494329), 2790889492)

	def test_subtract_neg_largenums(self):
		self.assertEqual(self.bmo.subtract(-7529383821, -4738494329), -2790889492)

	def test_multiply_pos(self):
		self.assertEqual(self.bmo.multiply(3, 4), 12)

	def test_multiply_neg(self):
		self.assertEqual(self.bmo.multiply(-3, -4), 12)

	def test_multiply_pos_neg(self):
		self.assertEqual(self.bmo.multiply(3, -4), -12)

	def test_multiply_zero(self):
		self.assertEqual(self.bmo.multiply(0, 4), 0)

	# method fails because 2 values are required per the class definition
	# def test_multiply_value_missing(self):
	# 	self.assertEqual(self.bmo.multiply(3,), 0)

	# method fails because 2 values are required per the class definition
	# def test_multiply_none(self):
	# 	self.assertEqual(self.bmo.multiply(), )

	def test_multiply_pos_largenums(self):
		self.assertEqual(self.bmo.multiply(383821, 494329), 189733851109)

	def test_multiply_neg_largenums(self):
		self.assertEqual(self.bmo.multiply(383821, -494329), -189733851109)

	def test_divide_pos(self):
		self.assertEqual(self.bmo.divide(20, 4), 5)

	def test_divide_neg(self):
		self.assertEqual(self.bmo.divide(-20, -4), 5)

	def test_divide_pos_neg(self):
		self.assertEqual(self.bmo.divide(20, -4), -5)

	# method fails because of division by zero error
	# def test_divide_zero(self):
	# 	self.assertEqual(self.bmo.divide(20, 0), 5)

	# method fails because 2 values are required per the class definition
	# def test_divide_value_missing(self):
	# 	self.assertEqual(self.bmo.divide(20,), 5)

	# method fails because 2 values are required per the class definition
	# def test_divide_none(self):
	# 	self.assertEqual(self.bmo.divide(), )

	def test_divide_pos_largenums(self):
		self.assertEqual(self.bmo.divide(4829587185, 5), 965917437)

	def test_divide_neg_largenums(self):
		self.assertEqual(self.bmo.divide(4829587185, -5), -965917437)


if __name__ == '__main__':
	unittest.main()