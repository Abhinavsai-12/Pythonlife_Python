# String Contains Only a Certain Set of Characters

import re

def is_allowed(string):
    chare=re.compile(r'[^A-za-z0-9]')
    string=chare.search(string)
    return not bool(string)

print(is_allowed("Abcd1234"))
print(is_allowed("@#$%^"))
