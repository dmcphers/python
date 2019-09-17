import unittest

from strings import concat


class TestStrings(unittest.TestCase):

    def test_st_alpha_concat(self):
        data = ["Drew ", "McPherson"]
        result = concat(data)
        self.assertEqual(result, "Drew McPherson")

    def test_st_alphanum_concat(self):
        data = ["Drew ", "2019 ", "McPherson"]
        result = concat(data)
        self.assertEqual(result, "Drew 2019 McPherson")

    def test_st_num_concat(self):
        data = ["9 ", "16 ", "2019"]
        result = concat(data)
        self.assertEqual(result, "9 16 2019")

    def test_st_specl_concat(self):
        data = ["Drew ", "????? ", "McPherson ", "!!!!!"]
        result = concat(data)
        self.assertEqual(result, "Drew ????? McPherson !!!!!")

    def test_st_apostrophe(self):
        data = ["I don't think so"]
        result = concat(data)
        self.assertEqual(result, "I don't think so")

    def test_st_quote(self):
        data = ['He said, "I see it"']
        result = concat(data)
        self.assertEqual(result, 'He said, "I see it"')

    def test_st_escape_char(self):
        data = ['I don\'t think so']
        result = concat(data)
        self.assertEqual(result, "I don't think so")


if __name__ == '__main__':
    unittest.main()