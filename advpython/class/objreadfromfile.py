class Student:
    def __init__(self,name,age):
        self.name=name
        self.age=age
    def printdata(self):
        print("name :",self.name)
        print("age :",self.age)

f=open("objfile","r")
for i in f:
    word=i.rstrip("\n").split(",")
    name=word[0]
    age=word[1]
    obj=Student(name,age)
    obj.printdata()