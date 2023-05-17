#!/usr/bin/python3
from sys import argv
add = 0
for i in range(len(argv) - 1):
    add += int(argv[i + 1)

print("{:d}".format(add))
