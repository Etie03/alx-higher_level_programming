#!/usr/bin/python3
for m in reversed(range(97, 123)):
    if (m % 2 == 0):
        print('{:c}'.format(m), end='')
    else:
        print('{:c}'.format(m - 32), end='')
