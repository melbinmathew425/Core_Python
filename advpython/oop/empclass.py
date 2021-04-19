class employee:
    def empval(self,rollno,name,salary):
        self.name=name
        self.rollno=rollno
        self.salary=salary
    def printemp(self):
        print("name",self.name )
        print("rollno",self.rollno)
        print("salary",self.salary)
obj = employee()
obj.empval("raju",1001,25000)
#obj.empval("rahul",1002,24000)
obj.printemp()
