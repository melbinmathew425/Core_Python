import re
d=input("enter")
rl="^[A-Z]+[a-z]+$"
match=re.fullmatch(rl,d)
if match is not None:
    print("valid")
else:
    print("invalid")