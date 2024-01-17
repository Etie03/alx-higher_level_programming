#!/usr/bin/python3
n = 1
for m in range(0, 8):
    for p in range(n, 10):
        print("{:d}{:d}".format(m, p), end=', ')
    n = n + 1
print("89")
