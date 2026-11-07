# number divisible by 7 but not multiply with 5

for i in range(1,100):
    if i%7==0 and i%5!=0:
        print('the number divisible by 7 but not multiply with 5:', i)