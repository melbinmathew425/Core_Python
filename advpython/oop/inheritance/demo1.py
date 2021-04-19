#single inheritance

class parent:#parentclass base class superclass
    parent_name="arun"
    def m1(self,age):
        self.age=age
        print("my name is ",parent.parent_name)
        print(self.age)
class child(parent):#derived class
    def m2(self,cage):
        self.cage=cage
        print("parentn name is ",parent.parent_name)
        print(self.age)
        print(self.cage)
c=child()
c.m1(23)
c.m2(25)

