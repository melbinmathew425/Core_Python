class Org:
    def cmp(self,cname):
        self.cname=cname
        print("cname ;",self.cname)
class Penssion(Org):
    def amt(self,pamt):
        self.pamt=pamt
        print("your pension amount ",self.pamt)
class Emp(Penssion):
    def id(self,name):
        self.name=name
        print("name :",self.name)

obj=Emp()
obj.cmp("luminar")
obj.id("melbin")
obj.amt(3200)