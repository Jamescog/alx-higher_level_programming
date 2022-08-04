#!/usr/bin/python3
if __name__ = "__main__":
    from sys import argv

    n = len(argv) - 1
    if n == 0:
        print("{} arguments.".format(n))
    elif n == 1:
        print("{} argument:".format(n))
        print("{}: {}".format(n, argv[n+1]))
    else:
        print("{} arguments:".format(n))
        for i in range(1, n):
            print("{}: {}".format(i, argv[i]))
