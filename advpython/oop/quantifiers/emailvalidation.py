import re
mail="melbin95@gmail.com"
rl="[a-zA-Z0-9]+@[a-zA-Z0-9]+\.[a-zA-Z]+$"
match=re.fullmatch(rl,mail)
if match is not None:
    print("valid")
else:
    print("invalid")