import re
n="56kg"
x='[a-z0-9]{4}'
match=re.fullmatch(x,n)
if match is not None:
    print("valid")
else:
    print("invalid")