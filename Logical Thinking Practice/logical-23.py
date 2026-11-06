# Access Index of a List Using for Loop
# Start indexing with a non-zero value

my_list=[22,12,15,16,11]

for index,val in enumerate(my_list, start=1):
    print(index, val)