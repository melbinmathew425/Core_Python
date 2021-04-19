lst=[[1001,"arun",17500],
     [1002,"melbin",15000],
     [1003,"hari",16500],
     [1004,"kiran",22000]]
t=0
for i in lst:
    t+=i[2]
    if(i[2]>17000):
        print(i[1])
print(t)