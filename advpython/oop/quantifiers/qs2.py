import re
d=input("enter the string")
rl="^[aA][a-zA-z0-9]*[bB]$"#  [a-zA_Z]* we can  type a-zA_Z0-9 or we can type nothing
match=re.fullmatch(rl,d)
if match is not None:
    print("valid")
else:
    print("invalid")