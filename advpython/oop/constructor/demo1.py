class person:
    def __init__(self,name,age):#it used to initialize the instant variable
        self.name=name
        self.age=age
    def printval(self):
        print("name :",self.name)
        print("age :",self.age)
obj=person("melbin",26)#using constructor we can directly give arguments of function when an object is creating
obj.printval()