#!/usr/bin/python3
for ch in range(97, 123):
    if ch == 'e' or ch == 'q':
        continue
    print("{:c}".format(ch), end="")
