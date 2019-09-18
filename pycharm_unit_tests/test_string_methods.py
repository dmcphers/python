

# Class to handle string methods
class StringMethods:
    a = ""

    def __init__(self):
        pass

    # capitalize method
    def capitalize(self, a):
        self.a = a
        return a.capitalize()


if __name__ == '__main__':
    strMeth = StringMethods()
    print(strMeth.capitalize("he is here."))
