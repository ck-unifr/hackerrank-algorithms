#!/bin/python3

import os
import sys

#
# Complete the birthdayCakeCandles function below.
#
def birthdayCakeCandles(n, ar):
    max_height = max(ar)
    nb_max_height = 0
    for val in ar:
        if max_height == val:
            nb_max_height += 1
    return nb_max_height


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    ar = list(map(int, input().rstrip().split()))

    result = birthdayCakeCandles(n, ar)

    f.write(str(result) + '\n')

    f.close()
