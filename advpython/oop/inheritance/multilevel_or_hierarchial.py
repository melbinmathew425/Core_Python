class Parent:
    def m1(self):
        print("inside parent")
class Child(Parent):
    def m2(self):
        print("inside child")
class Subchild(Child):
    def m3(self):
        print("inside subchild")
obj=Subchild()
obj.m1()
obj.m2()
obj.m3()
obj1=Child()
obj1.m1()
obj1.m2()
obj1.m3()#we can't inherit child from sub child
