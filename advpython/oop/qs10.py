import re
d=input("enter the string")
rl="^[aA][a-zA-z0-9]*[bB]$"
match=re.fullmatch(rl,d)
if match is not None:
    print("Its Matching")
else:
    print("Its not matched")