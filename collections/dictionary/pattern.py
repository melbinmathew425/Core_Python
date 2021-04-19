p="ABCDEFA"
dic={}
for i in p:
    if (i not in dic):
        dic[i]=1
    else:
        print(i)
        break