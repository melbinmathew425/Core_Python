import re
x="a+"#print only 'a' including group
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())