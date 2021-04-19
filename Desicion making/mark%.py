m1=int(input("Mark of sub1 : "))
m2=int(input("Mark of sub2 : "))
m3=int(input("Mark of sub3 : "))
m4=int(input("Mark of sub4 : "))
s=m1+m2+m3+m4
p=(s*100)/200
if(p<=100&p>=90):
    print("A+")
elif(p<=89&p>=80):
    print("A")
elif(p<=79&p>=70):
    print("B+")
elif(p<=69&p>=60):
    print("B")
elif(p<=59&p>=50):
    print("C+")
elif(p<=49&p>=40):
    print("c")
elif(p<=39&p>=30):
    print("D+")
else:
    print("FAIL")