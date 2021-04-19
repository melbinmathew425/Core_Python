no=int(input("Enter a no."))        #153
res=0
while(no!=0):
    a=no%10
    res=(res*10)+a
    no=no//10
print(res)
