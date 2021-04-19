import re
x="a*"#count 'a' and all athors,but print only 'a'(print only group of a)
r="aaa abc aaaa cga"
matcher=re.finditer(x,r)
for match in matcher:
    print(match.start())
    print(match.group())