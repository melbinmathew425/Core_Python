class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark

    def printdata(self):
        print(self.name)
        print(self.rollno)
        print(self.course)
        print(self.mark)
lst=[]
f=open("qfile1")
for i in f:
    name,rollno,course,mark=i.rstrip("\n").split(",")
    s1=Student(name,rollno,course,mark)
    lst.append(s1)
mark=[]
for st in lst:
    mark.append(st.mark)
hm=max(mark)
for st in lst:
    if (st.mark==hm):
        print(st.rollno,st.name,st.course,st.mark)
