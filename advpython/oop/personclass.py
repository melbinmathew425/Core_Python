class person:
    def setval(self,name,age):
        self.name=name
        self.age=age
    def printval(self):
        print("name :",self.name)
        print("age :",self.age)
obj=person()
obj.setval("melbin",26)
obj.printval()