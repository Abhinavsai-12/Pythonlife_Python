# Check if the first and last number is same in the list

numbers = [1,2,4,6,8,1]

def first_last(numbers):

    first=numbers[0]
    last=numbers[-1]

    if first == last:
        return True
    else:
        return False

print(first_last(numbers))
