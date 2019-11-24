

# Class to handle string methods
class StringMethods:
    a = ""
    # text1 = ""

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

    # center method
    def center(self, a):
        self.a = a
        x1 = a.center(20)
        return x1

    # count method
    def count(self, a):
        self.a = a
        return a.count("the")

    # endswith method
    def endswith(self, a):
        self.a = a
        return a.endswith("n")

    # expandtabs method
    def expandtabs(self, a):
        self.a = a
        return a.expandtabs(4)

    # find method
    def find(self, a):
        self.a = a
        return a.find("fell")

    # format method
    def format(self, a):
        self.a = a
        price = 50
        return a.format(price=50)

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

    # isprintable method
    def isprintable(self, a):
        self.a = a
        return a.isprintable()

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

    # join method
    def join(self):
        mytuple = ("Ray", "John", "Lisa")
        x = "#".join(mytuple)
        return x

    # ljust method
    def ljust(self, a):
        self.a = a
        myteam = a.ljust(20)
        return myteam, 'is my favorite team'

    # lower method
    def lower(self, a):
        self.a = a
        return a.lower()

    # lstrip method
    def lstrip(self, a):
        self.a = a
        return a.lstrip(), "is where I was born"

    # partition method
    def partition(self, a):
        self.a = a
        mypartition = a.partition("move")
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
        myrsplit = a.rsplit(",")
        return myrsplit

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
        return "What time does the", a.strip(), "open up?"

    # swapcase method
    def swapcase(self, a):
        self.a = a
        return a.swapcase()

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


if __name__ == '__main__':
    strMeth = StringMethods()
    print(strMeth.capitalize("he is here."))
    print(strMeth.casefold("HEY YOU!"))
    print(strMeth.center("origin"))
    print(strMeth.count("the guy fell over onto the mat when he tried to do the yoga pose"))
    print(strMeth.endswith("origin"))
    print(strMeth.expandtabs("H\te\tl\tl\to"))
    print(strMeth.find("the guy fell over onto the mat when he tried to do the yoga pose"))
    print(strMeth.format("The price is only {price:.2f} dollars!"))
    print(strMeth.index("the guy fell over onto the mat when he tried to do the yoga pose"))
    print(strMeth.isalnum("originof42"))
    print(strMeth.isalpha("originofthespecies"))
    # following isdecimal test should be false because code is unicode for letter D
    print(strMeth.isdecimal("\u0044"))
    print(strMeth.isdigit("50000"))
    print(strMeth.isidentifier("MyAwesomeFile"))
    print(strMeth.islower("MyAwesomeFile"))
    print(strMeth.isnumeric("4734729"))
    print(strMeth.isprintable("My dog is a senior now"))
    print(strMeth.isspace("    "))
    print(strMeth.istitle("My Dog Is A senior Now"))
    print(strMeth.isupper("MY DOG IS a SENIOR NOW!"))
    print(strMeth.join())
    print(strMeth.ljust("Texas"))
    print(strMeth.lower("WHERE ARE YOU GOING?"))
    print(strMeth.lstrip("     Houston     "))
    print(strMeth.partition("I would like to move to the city someday"))
    print(strMeth.replace("The cat jumped over the dog"))
    print(strMeth.rfind("To be or not to be, that is the question."))
    print(strMeth.rindex("To be or not to be, that is the question."))
    print(strMeth.rsplit("Sam, Max, Jason, John"))
    print(strMeth.splitlines("To be or not to be\nthat is the question."))
    print(strMeth.startswith("Austin is the capital."))
    print(strMeth.strip("     store     "))
    print(strMeth.swapcase("Sam, Max, Jason, John"))
    print(strMeth.title("once upon a time"))
    print(strMeth.upper("once upon a time"))
    print(strMeth.zfill("5181"))