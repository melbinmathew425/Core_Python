class calc:
    def __init__(self,no1,no2):
        self.no1=no1
        self.no2=no2
    def add(self):
        print("sum =",self.no1+self.no2)
    def diff(self):
        print("difference =", self.no1 - self.no2)#or return self.no1-self.no2-----*
    def mul(self):
        print("multiplication =",self.no1*self.no2)
    def div(self):
            print("division =", self.no1 / self.no2)
obj=calc(10,5)
obj.add()
obj.diff()#print(obj.diff())-------------------------------------------------------*
obj.mul()
obj.div()