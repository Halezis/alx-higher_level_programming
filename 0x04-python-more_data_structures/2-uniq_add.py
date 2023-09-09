#!/usr/bin/python3
def uniq_add(my_list=[]):
    new_items = []
    sum = 0
    for item in my_list:
        if item not in new_items:
            new_items.append(item)
            sum = sum + item
    return sum

