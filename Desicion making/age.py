bd=int(input("enter your date of birth : "))
td=int(input("todays date : "))
bm=int(input("enter your month of birth : "))
tm=int(input("todays month : "))
by=int(input("enter your year of birth : "))
ty=int(input("todays year : "))
age=ty-by
if bm==tm:
    if bd<=td:
      print("age :",age)
    else:
      print("age : 11 months and ",31-(bd-td),"days")
elif(bm-tm)>0:
    if(ty-by)>1:
        print("age :",age-1)
    else:
        print("age :", bm - tm, "months")
elif(tm-bm)>0:
    print("age :",age)