import unittest

from strings import concat, st_multiply, st_slice, st_length

# def concat(arg):
#     st_concat = ""
#     for val in arg:
#         st_concat += val
#     return st_concat
#
# def st_multiply(arg):
#     st_multiply = arg * 5
#     return st_multiply
#
# def st_slice(arg):
#     st_slice_st = arg[:7]
#     return st_slice_st
#
# def st_length(arg):
#     st_len = len(arg)
#     return st_len

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

    def test_st_newline_char(self):
        data = ['C:\Drew\Desktop\nPics']
        result = concat(data)
        print(result)
        self.assertEqual(result, "C:\Drew\Desktop" + "\n" + "Pics")

    def test_st_raw(self):
        data = [r'C:\Drew\Desktop\nPics']
        result = concat(data)
        print(result)
        self.assertEqual(result, r"C:\Drew\Desktop\nPics")

    def test_st_multiply(self):
        data = "Drew "
        result = st_multiply(data)
        print(result)
        self.assertEqual(result, "Drew Drew Drew Drew Drew ")

    def test_st_slice_string(self):
        data = "Tuna McFish"
        result = st_slice(data)
        print(result)
        self.assertEqual(result, "Tuna Mc")

    def test_st_length(self):
        data = "Tuna McFish"
        result = st_length(data)
        print(result)
        self.assertEqual(result, 11)


if __name__ == '__main__':
    unittest.main()