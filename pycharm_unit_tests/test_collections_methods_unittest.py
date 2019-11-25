import unittest


# class to handle collections methods
class CollectionsMethods:

    a = []
    b = ()

    def __init__(self):
        pass

# list append method
    def append(self, a):
        self.a = a
        a.append("Skunk")
        return a

# list count method
    def list_count(self, a):
        self.a = a
        return a.count("Dog")

# list index method
    def index(self, a):
        self.a = a
        return a.index("Burrito")

# list insert method
    def insert(self, a):
        self.a = a
        a.insert(1, "Mazda")
        return a

# list pop method
    def pop(self, a):
        self.a = a
        a.pop(1)
        return a

# list remove method
    def remove(self, a):
        self.a = a
        a.remove("Chevy")
        return a

# list reverse method
    def reverse(self, a):
        self.a = a
        a.reverse()
        return a

# list sort method
    def sort(self, a):
        self.a = a
        a.sort()
        return a

# tuple count method
    def tuple_count(self, b):
        self.b = b
        return b.count("Dog")

# tuple index method
    def tuple_index(self, b):
        self.b = b
        return b.index(11)


class TestCollectionsMethods(unittest.TestCase):
    def setUp(self):
        self.tcm = CollectionsMethods()

    def test_list_append(self):
        self.assertEqual(self.tcm.append(['Dog','Cat','Fox']), ['Dog','Cat','Fox','Skunk'])

    def test_list_count(self):
        self.assertEqual(self.tcm.list_count(['Dog','Cat','Dog','Penguin','Dog','Fox']), 3)

    def test_list_index(self):
        self.assertEqual(self.tcm.index(['Ice cream','Pizza','Burrito']), 2)

    def test_list_insert(self):
        self.assertEqual(self.tcm.insert(['Ford','Chevy','Dodge']), ['Ford','Mazda','Chevy','Dodge'])

    def test_list_pop(self):
        self.assertEqual(self.tcm.pop(['Ford','Mazda','Chevy','Dodge']), ['Ford','Chevy','Dodge'])

    def test_list_remove(self):
        self.assertEqual(self.tcm.remove(['Ford','Mazda','Chevy','Dodge']), ['Ford','Mazda','Dodge'])

    def test_list_reverse(self):
        self.assertEqual(self.tcm.reverse(['Ford','Mazda','Chevy','Dodge']), ['Dodge','Chevy','Mazda','Ford'])

    def test_list_sort(self):
        self.assertEqual(self.tcm.sort(['Ford','Mazda','Chevy','Dodge']), ['Chevy','Dodge','Ford','Mazda'])

    def test_tuple_count(self):
        self.assertEqual(self.tcm.tuple_count(('Dog','Cat','Dog','Penguin','Dog','Fox','Dog')), 4)

    def test_tuple_index(self):
        self.assertEqual(self.tcm.tuple_index((44,35,29,18,27,11,55)), 5)


if __name__ == '__main__':
    unittest.main()