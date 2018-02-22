#!/usr/bin/python

import sys


def main():
    for line in sys.stdin:
        words = line.strip().split()
        for word in words:
            if len(word) == 3 or len(word) == 5:
                print("%s\t1" % word)


if __name__ == "__main__":
    main()