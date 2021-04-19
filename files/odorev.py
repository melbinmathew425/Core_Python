f=open("ref_file1","r")
ev=[]
od=[]
lst=[]
for j in f:
    lst.append(int(j.rstrip("\n")))
    if (int(j)%2==0):
        ev.append(int(j.rstrip("\n")))
    else:
        od.append(int(j.rstrip("\n")))
print("list =", lst)
print("odd list =",od)
print("even list =",ev)
print("odd sum =",sum(od))
print("even sum =",sum(ev))