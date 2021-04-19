class Student:
    def __init__(self,name,rollno,course,mark):
        self.name=name
        self.rollno=rollno
        self.course=course
        self.mark=mark

    def printdata(self):
        print("name :",self.name)
        print("rollno :",self.rollno)
        print("course :", self.course)
        print("mark :", self.mark)

f=open("objfile2","r")
for i in f:
    word=i.rstrip("\n").split(",")
    name=word[0]
    rollno=word[1]
    course=word[2]
    mark=int(word[3])
    obj=Student(name,rollno,course,mark)
    if(190<mark):
        obj.printdata()
