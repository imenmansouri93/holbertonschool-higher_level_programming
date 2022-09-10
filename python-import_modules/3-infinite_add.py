#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    sum = 0
    for i in range (len(sys.argv) - 1):
        sum += int(sys.arg[i+1])
    print("{}".format(sum))