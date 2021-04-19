class Emp:
    cmpname="Luminar"
    def __init__(self,empname,empno):
        self.empname=empname
        self.empno=empno
    def printdata(self):
        print(Emp.cmpname)
        print(self.empname)
        print(self.empno)
    def __str__(self):
        return self.empname+str(self.empno)
re=Emp("arun",45)
print(re)