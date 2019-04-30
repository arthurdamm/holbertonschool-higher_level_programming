#!/usr/bin/python3
for i in range(ord('a'), ord('z') + 1):
    print("{:c}".format(i), end="\n" if i == 122 else "")
