import re
lst=[]
x='[a-zA-Z]{2}\d{2}[a-zA-Z]{2}\d{4}'
f=open("vehfile","r")
for i in f:
    num=i.rstrip("\n")
    match=re.fullmatch(x,num)
    if match is not None:
        lst.append(num)
print(lst)
