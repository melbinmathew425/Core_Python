class College:
    clgname="MAC"

    def __init__(self,name,rollno):
        self.name=name
        self.rollno=rollno
    def printdata(self):
        print("clge nsme ",College.clgname)
        print("name of student",self.name)
        print("rollno",self.rollno)
    def __str__(self):
        return self.name+str(self.rollno)
obj=College("anu",4)
print(obj)


