#!/usr/bin/python3

import sys

count = len(sys.argv) - 1
if count == 0:
    print("0 arguments.")
elif count == 1:
    print("1 argument:")
else:
    print("{:d} arguments:".format(count))
for i in range(count):
    print("{:d}: {:d}".format(i + 1, sys.argv[i + 1]))
