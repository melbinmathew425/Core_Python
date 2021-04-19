import re
chara=input("Enter ")
rl="[a-zA-Z]+\d{1}$"
match=re.fullmatch(rl,chara)
if match is not None:
    print("valid")
else:
    print("invalid")