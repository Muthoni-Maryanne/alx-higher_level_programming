#!/usr/bin/python3
i = 0
for i in range(i, 10):
    for j in range(i + 1, 10):
        if i == 8 and j == 9:
            print(f"{i}{j}")
            break
        print(f"{i}{j}", end=', ')
