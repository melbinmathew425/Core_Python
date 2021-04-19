import re
lst=[]
rl="[L][U][M]\d{2}[P][Y]\d{3}$"
f=open("ipfile","r")
f2=open("opfile","w")
for i in f:
    data=i.rstrip("\n")
    match=re.fullmatch(rl,data)
    if match is not None:
        f2.write(data)
        f2.write("\n")


