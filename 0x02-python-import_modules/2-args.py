#!/usr/bin/python3

import sys

if __name__ == "__main__":
    i = 1

    if (len(sys.argv) - 1) == 0:
        print("0 arguments.")
    elif (len(sys.argv) - 1) == 1:
        print("1 argument:")
    elif (len(sys.argv) - 1) > 1:
        print("{} arguments:".format(len(sys.argv) - 1))
    while i < len(sys.argv):
        print("{}: {}".format(i, sys.argv[i]))
        i += 1
