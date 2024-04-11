#!/usr/bin/python3

import sys

if __name__ == "__main__":
    i = 1
    total = 0

    if len(sys.argv) - 1 == 0:
        print("0")
    elif len(sys.argv) - 1 == 1:
        a = int(sys.argv[1])
        print("{:d}".format(a))
    else:
        while i < len(sys.argv):
            a = int(sys.argv[i])
            total += a
            i += 1
        print("{:d}".format(total))
