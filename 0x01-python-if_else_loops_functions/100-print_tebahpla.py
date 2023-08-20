#!/usr/bin/python3
alphabets = ""
for i in range(122, 96, -1):
    if i % 2 == 0:
        alphabets += chr(i)
    elif i % 2 != 0:
        alphabets += chr(i - 32)
print("{}".format(alphabets), end="")
