# How to print half pyramid using *

rows = int(input("Enter no of rows you need:"))
for i in range(rows):
    for j in range(i+1):
        print("*", end=" ")
    print()