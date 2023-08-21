#!/usr/bin/python3

import sys

args = len(sys.argv) - 1
sum = 0

if __name__ == "__main__":
    if args == 0:
        print(0)
    else:
        for i in range(args):
            sum += int(sys.argv[i + 1])
        print(sum)
