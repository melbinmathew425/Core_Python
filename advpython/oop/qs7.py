import re
lst=[]
x='[+][9][1]\d{10}'
f=open("qfile2","r")
for i in f:
    num=i.rstrip("\n")
    match=re.fullmatch(x,num)
    if match is not None:
        print("valid")
    else:
        print("invalid")