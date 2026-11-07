# Recursive List Sum

def list_sum(numbers):
    if len(numbers) == 0:
        return 0
    else:
        return numbers[0] + list_sum(numbers[1:])


my_list = [10, 20, 30, 40, 50]
print("Sum of List:", list_sum(my_list))