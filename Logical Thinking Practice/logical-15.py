# Multiplication Table (from 1 to 10)

num=int(input("Enter a number to generate a particular table:"))

for i in range(1,11):
    print(num, 'X', i, '=', num*i)