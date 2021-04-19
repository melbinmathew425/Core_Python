import re
d=input("enter")
rl='[a-zA-Z]{8,15}'
match=re.fullmatch(rl,d)
if match is not None:
    print("valid")
else:
    print("invalid")