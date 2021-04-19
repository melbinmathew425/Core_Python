import re
x = "[a-z]"#all from a to z,enly letters, except space
matcher = re.finditer (x , "abt c@5kz")
for match in matcher:
    print(match.start())
    print(match.group())