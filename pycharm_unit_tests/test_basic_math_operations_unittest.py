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
	bmo = BasicMathOperations()
	print(bmo.add(4,5))
	print(bmo.multiply(4,5))
	print(bmo.divide(20,4))
	print(bmo.subtract(4,5))