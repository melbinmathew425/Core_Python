f=open("ref_file1","r")
lst=[]
for num in f:
   lst.append(int(num.rstrip("\n")))#here we use rstrip() for removing the"\n" from right side
   #int() is used for converting list of string to the int of string
print(lst)
print(sum(lst))