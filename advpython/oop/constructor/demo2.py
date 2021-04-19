class employee:
    def __init__(self,rollno,name,salary):
        self.name=name
        self.rollno=rollno
        self.salary=salary
    def printemp(self):
        print("name",self.name )
        print("rollno",self.rollno)
        print("salary",self.salary)
obj = employee("raju",1001,25000)
obj.printemp()