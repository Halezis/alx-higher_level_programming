#!/usr/bin/python3

def remove_char_at(str, n):
    index = 0
    copy=""
    for char in str:
        if index == n:
            index += 1
            continue
        else:
            copy += char
            index += 1
    return copy
