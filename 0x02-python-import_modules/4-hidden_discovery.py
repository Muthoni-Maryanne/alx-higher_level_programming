#!/usr/bin/python3

import hidden_4

if __name__ == "__main__":
    a = dir(hidden_4)
    for i in a:
        if not i.startswith('__') and not i.endswith('__'):
            print(i)
