# Extend list without Append

list1 = [10, 20, 30]
list2 = [40, 50, 60]

result = list1 + list2
print(result)


l1=[1,2,3,4]
l2=[5,6,7,8]

l1[:0]=l2
print(l1)