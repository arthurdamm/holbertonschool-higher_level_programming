#!/usr/bin/python3
if __name__ == "__main__":
    import sys
    l = len(sys.argv) - 1
    print("{} argument{}{}"
          .format(l, "" if l == 1 else "s", "." if l == 0 else ":"))
    for i in range(l):
        print("{}: {}".format(i + 1, sys.argv[i + 1]))
