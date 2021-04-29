#!/usr/bin/python3
import sys

if __name__ == '__main__':
    av = sys.argv
    nargs = len(av)
    sum = 0
    if nargs > 1:
        for i in range(1, nargs):
            sum += int(av[i])
    print(sum)
