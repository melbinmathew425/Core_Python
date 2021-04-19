import re
x = "\s"#space check
matcher = re.finditer (x , "abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())