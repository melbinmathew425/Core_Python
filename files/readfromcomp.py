f=open("C:/Users/vargh/Desktop/customer","r")
for line in f:
   data=line.rstrip("\n").split(",")
   name=data[1]
   age=data[3]
   location=data[-1]
   print(name,age,location)

