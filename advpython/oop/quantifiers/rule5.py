import re
x="a{1,3}"#its print the group or individualy, when its no of 'a' is in between {1,3}
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())