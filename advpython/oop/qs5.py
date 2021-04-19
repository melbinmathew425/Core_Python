#overriding is a feature of python. if we create same functions in a inheritted calss, in the time of function call its consider only the function of the derived class
class Book:
    def introduction(self):
        print("in the 1st page")

class Book2(Book):
    def introduction(self):
        print("in the second page")
c=Book2()
c.introduction()