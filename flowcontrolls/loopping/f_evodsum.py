lwr=int(input("Enter the lower limit"))
upr=int(input("Enter the uper limit"))
es=0
os=0
for i in range(lwr,upr+1):
    if i%2==0:
        es=es+i
    else:
        os=os+i
print(es)
print(os)