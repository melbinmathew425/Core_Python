import re
x="a?"#print the all'a' idividually, it also read the positon or index of athor value bt not print
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())