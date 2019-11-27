import unittest


class StringTests:

    x = ""

    def __init__(self):
        pass

    def concat(self, *args):
        st_concat = ""
        for arg in args:
            st_concat += arg
        return st_concat

    def st_multiply(self, x):
        st_multiply = x * 5
        return st_multiply

    def st_slice(self, x):
        st_slice_st = x[:7]
        return st_slice_st

    def st_length(self, x):
        st_len = len(x)
        return st_len

    def st_reverse(self, x):
        st_rev = x[::-1]
        return st_rev


class TestStrings(unittest.TestCase):

    def setUp(self):
        self.st_test = StringTests()

    def test_st_alpha_concat(self):
        self.assertEqual(self.st_test.concat("Drew ", "McPherson"), "Drew McPherson")

    def test_st_alphanum_concat(self):
        self.assertEqual(self.st_test.concat("Drew ", "2019", " McPherson"), "Drew 2019 McPherson")

    def test_st_num_concat(self):
        self.assertEqual(self.st_test.concat("11 ", "24", " 2019"), "11 24 2019")

    def test_st_specl_concat(self):
        self.assertEqual(self.st_test.concat("Drew ", "????? ", "McPherson ", "!!!!!"), "Drew ????? McPherson !!!!!")

    def test_st_multiply(self):
        self.assertEqual(self.st_test.st_multiply("Drew "), "Drew Drew Drew Drew Drew ")

    def test_st_slice_string(self):
        self.assertEqual(self.st_test.st_slice("Tuna McFish"), "Tuna Mc")

    def test_st_length(self):
        self.assertEqual(self.st_test.st_length("Tuna McFish"), 11)

    def test_st_reverse(self):
        self.assertEqual(self.st_test.st_reverse("Tuna McFish"), "hsiFcM anuT")


if __name__ == '__main__':
    unittest.main()