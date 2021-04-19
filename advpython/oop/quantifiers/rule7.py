import re
x="a$"##its print the index and value of a string ending with 'a'
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())