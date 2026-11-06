# Accept a hyphen-separated sequence of words
# Print the sorted words

stringItems = input("Enter a hyphen seperated string")

words=stringItems.split('-')
words.sort()

print('-'.join(words))
