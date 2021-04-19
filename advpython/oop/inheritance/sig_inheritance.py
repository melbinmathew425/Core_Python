class Org:
    def cmp(self,cname):
        self.cname=cname
class Emp(Org):
    def id(self,name):
        self.name=name
        print("name :",self.name)
        print("company name :",self.cname)
obj=Emp()
obj.cmp("luminar")
obj.id("melbin")