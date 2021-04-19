class Book:
    def __init__(self, Library_name, book_name, author, pages):
        self.Library_name= Library_name
        self.book_name=book_name
        self.author= author
        self.pages=pages
    def printdata(self):
        print("Library name :",self.Library_name)
        print("Book name :", self.book_name)
        print("Author name :", self.author)
        print("pages :", self.pages)
obj=Book("asdd","LT Book","Robin",1250)
obj.printdata()