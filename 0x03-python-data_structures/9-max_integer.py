#!/usr/bin/python3

def max_integer(my_list=[]):
    if my_list == []:
        return None
    max_value = my_list[0]

    # Iterate through the list to find the maximum value
    for num in my_list:
        if num > max_value:
            max_value = num

    return max_value
