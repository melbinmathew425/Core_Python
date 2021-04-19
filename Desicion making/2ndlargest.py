no1=int(input("Enter no1"))
no2=int(input("Enter no2"))
no3=int(input("enter no3"))
if (no1>no2) & (no1>no3):
    if(no2>no3):
        print(no2,"is the second largest")
    else:
        print(no3," is the second largest")
elif(no2>no1)&(no2>no3):
    if(no1<no3):
        print(no3," is the second largest")
    else:
        print(no1," is the second largest")
elif (no3>no1)&(no3>no2):
    if (no1>no2):
        print(no1, " is the second largest")
    else:
        print(no2, " is the second largest")
