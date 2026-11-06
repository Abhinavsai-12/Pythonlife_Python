# Find Length of the String

text="Hello, I am Learning Python"

def string_length(text):
    count =0
    for char in text:
        count +=1
    return count

print(string_length(text))