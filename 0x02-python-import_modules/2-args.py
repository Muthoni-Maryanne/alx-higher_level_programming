#!/usr/bin/python3

import sys

if __name__ == "__main__":
    i = 1

    if len(sys.argv) <= 1:
        print("{} arguments.".format(len(sys.argv) - 1))
    else:
        print("{} arguments:".format(len(sys.argv) - 1))
        while i < len(sys.argv):
            print("{}: {}".format(i, sys.argv[i]))
            i += 1
