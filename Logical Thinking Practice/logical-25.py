# Split String with Multiple Delimiters

import re

text="Hello! I am Learning Python. Practicing, Logical Thinking"
# print(text.split())
# print(text.split('!'))
print(re.split(r'[!.,]',text))