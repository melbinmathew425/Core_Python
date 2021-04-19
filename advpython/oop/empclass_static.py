class employee:
    cname="luminar"
    def empval(self,rollno,name,salary):
        self.name=name
        self.rollno=rollno
        self.salary=salary
    def printemp(self):
        print("name :",self.name )
        print("rollno :",self.rollno)
        print("salary :",self.salary)
        print("company :",employee.cname)
obj = employee()
obj.empval("raju",1001,25000)
obj.printemp()
obj1=employee()
obj1.empval("rahul",1002,24000)
obj1.printemp()
