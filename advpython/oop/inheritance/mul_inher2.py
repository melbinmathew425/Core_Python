class Org:
    def cmp(self,cname):
        self.cname=cname
class Penssion:
    def amt(self):
        print("you are eligible for pention")
class Emp(Org,Penssion):
    def id(self,name):
        self.name=name
        print("name :",self.name)
        print("company name :",self.cname)
obj=Emp()
obj.cmp("luminar")
obj.id("melbin")
obj.amt()