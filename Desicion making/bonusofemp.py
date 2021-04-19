s=int(input("Enter your salary "))
y=int(input("Enter your years of experience "))
t=0
if(y>=5):
    t=s*.05
    s=s+t
    print("your bonus is",t)
    print("your new salary",s)
else:
    print("you are no eligible for the bonus")

