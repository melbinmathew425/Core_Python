class Person:
    houselocation="Cochin"
    def gd(self,grandfather):
        self.grandfather=grandfather
        print("My Grand father name : ",self.grandfather)
class Son(Person):
    def fd(self,fathername):
        self.fathername=fathername
        print("My father name :",self.fathername)

class Son1():
    def sdd(self):
        print("My house name : MG House")

class grandson(Son,Son1):
    def sd(self,name):
        self.name=name
        print("My name :",self.name)
        print("My house name :",Person.houselocation)
        print("")
obj=grandson()
obj.gd("Raj")
obj.fd("Arun Raj")
obj.sd("Dev Arun Raj")
obj.sdd()





