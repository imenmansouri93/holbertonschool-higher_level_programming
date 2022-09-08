#!/usr/bin/python3
for i in range(0, 99):
    print(i, end=' = ')
    print({}.format(hex(i)), end='')
    print("\n")
