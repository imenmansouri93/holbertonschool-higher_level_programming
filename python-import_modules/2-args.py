#!/usr/bin/python3
import sys
if __name__ == "__main__":
    av = len(sys.argv)
if av == 1:
    print("{} arguments.".format(av -  1))
elif av == 2:
    print("{} argument:".format(av -  1))
else:
    print("{} arguments:".format(av -  1))
for i in range(1, av):
    print("{}: {}".format(i, sys.argv[i]))
