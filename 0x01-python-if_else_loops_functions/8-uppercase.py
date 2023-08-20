#!/usr/bin/python3

def uppercase(str):
    for char in str:
        char_code = ord(char)
        if char_code >= 97 and char_code <= 122:
            upper_code = char_code - 32
            print("{}".format(chr(upper_code)), end="")
        else:
            print("{}".format(char), end="")
    print()
