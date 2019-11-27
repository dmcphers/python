import unittest


# Class to handle string methods
class StringMethods:
    a = ""

    def __init__(self):
        pass

    # capitalize method
    def capitalize(self, a):
        self.a = a
        return a.capitalize()

    # casefold method
    def casefold(self, a):
        self.a = a
        return a.casefold()

    # count method
    def count(self, a):
        self.a = a
        return a.count("the")

    # endswith method
    def endswith(self, a):
        self.a = a
        return a.endswith(".")

    # find method
    def find(self, a):
        self.a = a
        return a.find("fell")

    # index method
    def index(self, a):
        self.a = a
        return a.index("guy")

    # isalnum method
    def isalnum(self, a):
        self.a = a
        return a.isalnum()

    # isalpha method
    def isalpha(self, a):
        self.a = a
        return a.isalpha()

    # isdecimal method
    def isdecimal(self, a):
        self.a = a
        return a.isdecimal()

    # isdigit method
    def isdigit(self, a):
        self.a = a
        return a.isdigit()

    # isidentifier method
    def isidentifier(self, a):
        self.a = a
        return a.isidentifier()

    # islower method
    def islower(self, a):
        self.a = a
        return a.islower()

    # isnumeric method
    def isnumeric(self, a):
        self.a = a
        return a.isnumeric()

    # isspace method
    def isspace(self, a):
        self.a = a
        return a.isspace()

    # istitle method
    def istitle(self, a):
        self.a = a
        return a.istitle()

    # isupper method
    def isupper(self, a):
        self.a = a
        return a.isupper()

    # lower method
    def lower(self, a):
        self.a = a
        return a.lower()

    # partition method
    def partition(self, a):
        self.a = a
        mypartition = a.partition("is")
        return mypartition

    # replace method
    def replace(self, a):
        self.a = a
        myreplace = a.replace("dog", "horse")
        return myreplace

    # rfind method
    def rfind(self, a):
        self.a = a
        myfind = a.rfind("be")
        return myfind

    # rindex method
    def rindex(self, a):
        self.a = a
        myindex = a.rindex("to")
        return myindex

    # rsplit method
    def rsplit(self, a):
        self.a = a
        myrsplit = a.rsplit(", ")
        return myrsplit

    # split method
    def split(self, a):
        self.a = a
        mysplit = a.split()
        return mysplit

    # splitlines method
    def splitlines(self, a):
        self.a = a
        return a.splitlines()

    # startswith method
    def startswith(self, a):
        self.a = a
        return a.startswith("Austin")

    # strip method
    def strip(self, a):
        self.a = a
        return a.strip()

    # title method
    def title(self, a):
        self.a = a
        return a.title()

    # upper method
    def upper(self, a):
        self.a = a
        return a.upper()

    # zfill method
    def zfill(self, a):
        self.a = a
        return a.zfill(8)

    def append(self, x):
        testList = ['test']
        testList.append((x))
        return "".join(testList)


class TestStringMethods(unittest.TestCase):
    def setUp(self):
        self.tsm = StringMethods()

    def test_st_capitalize(self):
        self.assertEqual(self.tsm.capitalize("he is here"), "He is here")

    def test_st_casefold(self):
        self.assertEqual(self.tsm.casefold("Hey You"), "hey you")

    def test_st_count(self):
        self.assertEqual(self.tsm.count("the guy fell over onto the mat when he tried to do the yoga pose"), 3)

    def test_st_endswith(self):
        self.assertEqual(self.tsm.endswith("He is here."), True)

    def test_st_find(self):
        self.assertEqual(self.tsm.find("the guy fell over onto the mat when he tried to do the yoga pose"), 8)

    def test_st_index(self):
        self.assertEqual(self.tsm.index("the guy fell over onto the mat when he tried to do the yoga pose"), 4)

    def test_st_isalnum(self):
        self.assertEqual(self.tsm.isalnum("originof42"), True)

    def test_st_isalpha(self):
        self.assertEqual(self.tsm.isalpha("originofthespecies"), True)

    def test_st_isdecimal(self):
        self.assertEqual(self.tsm.isdecimal("\u0033"), True)

    def test_st_isdigit(self):
        self.assertEqual(self.tsm.isdigit("51555"), True)

    def test_st_isidentifier(self):
        self.assertEqual(self.tsm.isidentifier("My_awesome_id_101"), True)

    def test_st_islower(self):
        self.assertEqual(self.tsm.islower("he is here"), True)

    def test_st_isnumeric(self):
        self.assertEqual(self.tsm.isnumeric("5156517"), True)

    def test_st_isspace(self):
        self.assertEqual(self.tsm.isspace("   "), True)

    def test_st_istitle(self):
        self.assertEqual(self.tsm.istitle("My Dog Is A Senior Now"), True)

    def test_st_isupper(self):
        self.assertEqual(self.tsm.isupper("MY DOG IS A SENIOR NOW"), True)

    def test_st_lower(self):
        self.assertEqual(self.tsm.lower("WHERE ARE YOU GOING"), "where are you going")

    def test_st_partition(self):
        self.assertEqual(self.tsm.partition("My favorite team is the Longhorns"),
                         ('My favorite team ', 'is', ' the Longhorns'))

    def test_st_replace(self):
        self.assertEqual(self.tsm.replace("The cat jumped over the dog"), "The cat jumped over the horse")

    def test_st_rfind(self):
        self.assertEqual(self.tsm.rfind("To be or not to be, that is the question"), 16)

    def test_st_rsplit(self):
        self.assertEqual(self.tsm.rsplit("Sam, Max, Jake, Steven"), ['Sam', 'Max', 'Jake', 'Steven'])

    def test_st_split(self):
        self.assertEqual(self.tsm.split("Welcome to my world"), ['Welcome', 'to', 'my', 'world'])

    def test_st_splitlines(self):
        self.assertEqual(self.tsm.splitlines("To be or not to be\nthat is the question"),
                         ['To be or not to be', 'that is the question'])

    def test_st_startswith(self):
        self.assertEqual(self.tsm.startswith("Austin is the capital"), True)

    def test_st_strip(self):
        self.assertEqual(self.tsm.strip("     I see you     "), "I see you")

    def test_st_title(self):
        self.assertEqual(self.tsm.title("once upon a time"), "Once Upon A Time")

    def test_st_upper(self):
        self.assertEqual(self.tsm.upper("the cat is out of the bag"), "THE CAT IS OUT OF THE BAG")

    def test_st_zfill(self):
        self.assertEqual(self.tsm.zfill("50"), "00000050")

    def test_st_append(self):
        self.assertEqual(self.tsm.append("Append"), "testAppend")


if __name__ == '__main__':
    unittest.main()