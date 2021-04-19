c=int(input("enter your total no of classes  "))
a=int(input("Enter your attendence "))
p=(a*100)/c
print("your attendence is ",p,"%")
if(p>=75):
    print("you are eligible for write the exam")
else:
    print("you are not eligible for exam")
