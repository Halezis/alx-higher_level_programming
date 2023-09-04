#!/usr/bin/python3

def divisible_by_2(my_list=[]):
    # Create an empty list to store True/False values
    result = []

    # Iterate through the elements in the original list
    for num in my_list:
        # Check if the current number is divisible by 2
        if num % 2 == 0:
            result.append(True)
        else:
            result.append(False)

    return result
