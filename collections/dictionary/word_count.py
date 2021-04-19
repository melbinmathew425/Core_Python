line="hai hello hai hello hai"
word=line.split(" ")#split function used to split a sentence into words
dic={}
for i in word:
    if (i not in dic):
        dic[i]=1
    else:
        dic[i]+=1
print(dic)