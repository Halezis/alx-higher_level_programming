#!/usr/bin/python3
for i in range(97, 123):
    if i == 101 or i == 114:
        continue
    print("{0:s}".format(chr(i)), end="")
