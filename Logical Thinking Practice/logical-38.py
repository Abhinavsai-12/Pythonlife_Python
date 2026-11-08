# Caluclate lower case and upper case letters in a string
def String_Test(s):
    upper_case = 0
    lower_case = 0


    for i in s:
        if i.isupper():
            upper_case +=1

        elif i.islower():
            lower_case +=1

        else:
            pass

    print("Uppercase Letters:", upper_case)
    print("Lowercase Letters:", lower_case)
    


String_Test("Hi, Can you give me a chance")