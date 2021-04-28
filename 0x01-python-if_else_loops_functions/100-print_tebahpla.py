#!/usr/bin/python3
for i in reversed(range(ord("a"), ord("z")+1)):
    if (i % 2 == 0):
        print('{:c}'.format(i), end='')
    else:
        print('{:c}'.format(i - 32), end='')
