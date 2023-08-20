#!/usr/bin/python3

def uppercase(str):
    output = ""
    for char in str:
        char_code = ord(char)
        if char_code >= 97 and char_code <= 122:
            upper_code = char_code - 32
            output += chr(upper_code)
        else:
            output += char
    print("{}".format(output))
