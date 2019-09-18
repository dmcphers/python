import unittest


# Class to handle basic arithmetic operations
class ArithmeticFunctions():

	# Add function
	def addition(self, a, b):
		return a + b

	# Multiply function
	def multiply(self, a, b):
		return a * b

	# Divide function
	def divide(self, a, b):
		return a / b

	# Subtract function
	def subtract(self, a, b):
		return a - b


# Create an object of the ArithmeticFunctions Class
arithmetic_object = ArithmeticFunctions()


# Test class
class TestBasicOperations(unittest.TestCase):

	# test for addition function
	def test_addition(self):
		self.assertTrue(arithmetic_object.addition(2, 3) == 5)

	# test for multiplication
	def test_multiplication(self):
		self.assertTrue(arithmetic_object.multiply(3, 3) == 9)

	# test for division
	def test_division(self):
		self.assertTrue(arithmetic_object.divide(10, 5) == 2)

	# test for subtraction
	def test_subtraction(self):
		self.assertTrue(arithmetic_object.subtract(5, 5) == 0)


if __name__ == '__main__':
	unittest.main()