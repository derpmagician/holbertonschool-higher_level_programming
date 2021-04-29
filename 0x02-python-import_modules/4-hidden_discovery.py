#!/usr/bin/python3
import hidden_4

if __name__ == '__main__':
    definames = dir(hidden_4)

    for i in range(len(definames)):
        if definames[i][:2] != '__':
            print(definames[i])
