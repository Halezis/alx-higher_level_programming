#!/usr/bin/python3
def safe_print_list(my_list=[], x=0):
    count = 0
    try:
        for item in my_list:
            if count < x:
                print(item, end="")
                count += 1
            else:
                break
        print()
        return count
    except Exception as e:
        print(f"An error occured: {e}")
        return count
