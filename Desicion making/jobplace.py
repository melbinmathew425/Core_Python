ag=int(input("Enter your age "))
s=(input("enter your sex(ForM) "))
if (s=="m"):
    if(ag>20)&(ag<40):
        print("you should work anywhere")
    elif (ag>40)&(ag<60):
        print("you should work urban areas only")
else:
    print("you should work only in urban areas")