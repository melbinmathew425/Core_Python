#pattern matching
#regular expression is a package, used for the pattern matching

import re
count=0
matcher=re.finditer('ab','abaabbab')#finditer is a methord in re package
for match in matcher:
    count+=1
print("count :",count)
