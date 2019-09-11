import unittest

from numbers import sum, prod


class TestNumbers(unittest.TestCase):

    def test_sum(self):
        data = [3,4]
        result = sum(data)
        self.assertEqual(result, 7)

    def test_prod(self):
        data = [3,20]
        result = prod(data)
        self.assertEqual(result, 60)


if __name__ == '__main__':
    unittest.main()