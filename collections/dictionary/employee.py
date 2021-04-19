emp={"id":1001,"name":"melbin","designame":"manager","salary":25000}
print(emp["name"])
print("company" in emp)
emp["company"]="luminar"
emp["salary"]+=15000
for i in emp:
    print(i,",",emp[i])