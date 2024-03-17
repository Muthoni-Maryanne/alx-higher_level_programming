#!/usr/bin/python3
for i in range(10):
    for j in range(10):
        if i == 9 and j == 9:
            print(f"{i}{j}")
            break
        print(f"{i}{j}", end = ', ')
