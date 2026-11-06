# count the occurence of each word in the given sentence
def word_count(str):
    counts=dict()
    words=str.split()

    for word in words:
        if word in counts:
            counts[word] += 1
        else:
            counts[word]=1
    return counts


print(word_count('Hello, I am Learning Python for you . can you please see it. Thank you for everything'))