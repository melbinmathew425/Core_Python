class Person:
    housename="MG House"
    def __init__(self,grandfather):
        self.grandfather=grandfather
    def printdata(self):
        print("My Grand father name : ",self.grandfather)
class Son(Person):
    def __init__(self,fathername,grandfather):
        super().__init__(grandfather)
        self.fathername=fathername
    def print(self):
        print("My father name :",self.fathername)
class grandson(Person,Son):
    def __init__(self,name,fathername,grandfather):
        super().__init__(fathername,grandfather)
        self.name=name
    def pr(self):
        print("My name :",self.name)
        print("My house name :",Person.housename)
obj=grandson("Dev","ArunRaj","Raj")
obj.printdata()
obj.print()
obj.pr()