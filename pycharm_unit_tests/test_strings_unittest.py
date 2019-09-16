import unittest

from strings import concat


class TestStrings(unittest.TestCase):

    def test_st_alpha_concat(self):
        data = ["Drew ", "McPherson"]
        result = concat(data)
        self.assertEqual(result, "Drew McPherson")


if __name__ == '__main__':
        unittest.main()