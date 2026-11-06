# Removing whitespaces from a String

import re

text= " Learning     python"
print("Orginal Text:", text)
print("String After Removing white Spaces:", re.sub(r'\s+','',text))
print(text.replace(" ",''))