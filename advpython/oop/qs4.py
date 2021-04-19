class Animal:
    def __init__(self,type):
        self.type=type
    def printdata(self):
        print("Type of animal :",self.type)
class Dog(Animal):
    def __init__(self,name,type):
        super().__init__(type)
        self.name=name
    def printval(self):
        print("Name of dog :",self.name)
obj=Dog("Tippu","Domestic animal")
obj.printdata()
obj.printval()
