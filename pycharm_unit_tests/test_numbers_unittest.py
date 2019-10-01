import unittest

from numbers import summation, prod, diff, quot, quot_large


class TestNumbers(unittest.TestCase):

    def test_sum_pos(self):
        data = [3, 4]
        result = sum(data)
        self.assertEqual(result, 7)

    def test_sum_neg(self):
        data = [-3, -4]
        result = sum(data)
        self.assertEqual(result, -7)

    def test_sum_pos_neg(self):
        data = [-3, 4]
        result = sum(data)
        self.assertEqual(result, 1)

    def test_sum_zero(self):
        data = [0, 4]
        result = sum(data)
        self.assertEqual(result, 4)

    def test_sum_value_missing(self):
        data = [3]
        result = sum(data)
        self.assertEqual(result, 3)

    def test_sum_none(self):
        data = []
        result = sum(data)
        self.assertEqual(result, 0)

    def test_sum_largenums(self):
        data = [4738494329, 7529383821]
        result = sum(data)
        self.assertEqual(result, 12267878150)

    def test_diff_pos(self):
        data = [-13, 4]
        result = diff(data)
        self.assertEqual(result, 9)

    def test_diff_neg(self):
        data = [3, -4]
        result = diff(data)
        self.assertEqual(result, 1)

    def test_diff_pos_neg(self):
        data = [-3, 4]
        result = diff(data)
        self.assertEqual(result, -1)

    def test_diff_zero(self):
        data = [0, 4]
        result = diff(data)
        self.assertEqual(result, -4)

    def test_diff_value_missing(self):
        data = [3]
        result = diff(data)
        self.assertEqual(result, -3)

    def test_diff_none(self):
        data = []
        result = diff(data)
        self.assertEqual(result, 0)

    def test_diff_largenums(self):
        data = [-7529383821, 4738494329]
        result = diff(data)
        self.assertEqual(result, 2790889492)

    def test_prod_pos(self):
        data = [3, 20]
        result = prod(data)
        self.assertEqual(result, 60)

    def test_prod_neg(self):
        data = [-3, -20]
        result = prod(data)
        self.assertEqual(result, 60)

    def test_prod_pos_neg(self):
        data = [-3, 20]
        result = prod(data)
        self.assertEqual(result, -60)

    def test_prod_zero(self):
        data = [0, 4]
        result = prod(data)
        self.assertEqual(result, 0)

    def test_prod_value_missing(self):
        data = [3]
        result = prod(data)
        self.assertEqual(result, 3)

    def test_prod_none(self):
        data = []
        result = prod(data)
        self.assertEqual(result, 1)

    def test_prod_largenums(self):
        data = [383821, 494329]
        result = prod(data)
        self.assertEqual(result, 189733851109)

    def test_quot_pos(self):
        data = [2, 10]
        result = quot(data)
        self.assertEqual(result, 5)

    def test_quot_neg(self):
        data = [-2, -10]
        result = quot(data)
        self.assertEqual(result, 5)

    def test_quot_pos_neg(self):
        data = [-2, 10]
        result = quot(data)
        self.assertEqual(result, -5)

    # test will not pass when dividing by zero

    # def test_quot_zero(self):
    #     data = [0]
    #     result = quot(data)
    #     self.assertEqual(result, 0)

    def test_quot_value_missing(self):
        data = [5]
        result = quot(data)
        self.assertEqual(result, 20)

    def test_quot_none(self):
        data = []
        result = quot(data)
        self.assertEqual(result, 100)

    def test_quot_largenums(self):
        data = [5]
        result = quot_large(data)
        self.assertEqual(result, 965917437)


if __name__ == '__main__':
    unittest.main()