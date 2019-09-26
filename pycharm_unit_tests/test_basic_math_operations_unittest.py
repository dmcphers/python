import unittest


class TestBasicMathOperations(unittest.TestCase):
	def setUp(self):
		self.bmo = BasicMathOperations()

	def test_add(self):
		self.assertEqual(self.bmo.add(3, 4), 7)

	def test_subtract(self):
		self.assertEqual(self.bmo.subtract(4, 3), 1)

	def test_multiply(self):
		self.assertEqual(self.bmo.multiply(3, 4), 12)

	def test_divide(self):
		self.assertEqual(self.bmo.divide(20, 4), 5)


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


if __name__ == '__main__':
	unittest.main()