#!/usr/bin/python3

args = len(argv)

if __name__ == "__main__":
    if args == 0:
        print("0 arguments.")
    else:
        if args == 1:
            print("1 argument:")
        else:
            print("{} arguments:".format(args))
        for i in range(1, args + 1):
            print("{}: {}".format(i, argv[i]))
