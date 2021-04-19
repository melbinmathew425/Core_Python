class Parent:#parentclass base class superclass
    parent_name="arun"
    def m1(self,age):
        self.age=age
        print("my name is ",Parent.parent_name)
        print(self.age)
class Mobile:
    def mob(self):
        print(" i have mi")
class child(Parent,Mobile):#derived class
    def m2(self,cage):
        self.cage=cage
        print("parentn name is ",Parent.parent_name)
        print(self.age)
        print(self.cage)
c=child()
c.m1(23)
c.m2(25)
c.mob()