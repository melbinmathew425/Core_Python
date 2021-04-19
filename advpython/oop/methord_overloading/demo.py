#polymorphisum
 #overloading
class Person:
    def show(self,no1):
        self.no1=no1
        print("no1 ",self.no1)
class Student(Person):
    def show(self,no2,no3):
        self.no2=no2
        self.no3=no3
        print("no2  and no3",self.no2,self.no3)
obj=Student()
obj.show(3)

