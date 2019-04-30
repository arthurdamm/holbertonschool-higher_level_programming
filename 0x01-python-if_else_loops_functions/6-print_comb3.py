#!/usr/bin/python3
for i in range(10):
    for j in range(i, 10):
        if i < j:
            print("{:d}{:d}".format(i, j),
                  end="\n" if i is 8 and j is 9 else ", ")
