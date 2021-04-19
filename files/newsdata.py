f=open("ref_file2","r")
dic={}
for line in f:
    words=line.rstrip("\n").split(" ")
for j in words:
    if line not in dic:
        dic[j]=1
    else:
        dic[j]+=1
#for k in dic:
    #print(k,",",dic[k])
print(dic)