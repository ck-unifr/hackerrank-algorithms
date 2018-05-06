#https://www.hackerrank.com/challenges/plus-minus/problem

#!/bin/python3

import os
import sys

#
# Complete the plusMinus function below.
#
def plusMinus(arr):
    nb_pos = 0
    nb_neg = 0
    nb_zero = 0
    for val in arr:
        if val > 0:
            nb_pos += 1
        elif val < 0:
            nb_neg += 1
        else:
            nb_zero += 1

    print('{}'.format(round(nb_pos/len(arr), 6)))
    print('{}'.format(round(nb_neg / len(arr), 6)))
    print('{}'.format(round(nb_zero / len(arr), 6)))

if __name__ == '__main__':
    n = int(input())

    arr = list(map(int, input().rstrip().split()))

    plusMinus(arr)