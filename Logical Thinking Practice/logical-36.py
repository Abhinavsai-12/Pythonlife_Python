# Triple elements in list using map

num=(1,2,3,4,5,6,7,8)
result=map(lambda x:x+x+x, num)
print(list(result))