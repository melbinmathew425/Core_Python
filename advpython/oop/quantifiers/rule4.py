import re
x="a{3}"#its print the group of a, no of group mention in the {}
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())