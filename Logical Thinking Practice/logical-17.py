# write a program to detect the number of local variables declared in a function

a="v"
def Localvar():
    b=10
    V='A'
    x=2
    y=3
print(Localvar.__code__.co_nlocals)