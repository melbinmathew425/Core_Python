no=int(input("Enter a no :"))
for i in range(2,no):
    if no%i==0:
        flag=1
        break
    else:
        flag=0
if flag>0:
    print("its prime")
else:
    print("its not a prime")


