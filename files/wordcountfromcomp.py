f=open("C:/Users/vargh/Desktop/customer","r")
loc={}
for line in f:
    data = line.rstrip("\n").split(",")
    if data[-1] not in loc:
        loc[data[-1]]=1
    else:
        loc[data[-1]]+=1
print(loc)


