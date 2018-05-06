#https://www.hackerrank.com/challenges/diagonal-difference/problem

#!/bin/python3

import os
import sys

#
# Complete the diagonalDifference function below.
#
def diagonalDifference(a):
    length = len(a[0])
    sum1 = 0
    for i in range(length):
        sum1 += a[i][i]
    sum2 = 0
    for i in range(length):
        sum2 += a[i][length - i - 1]

    return abs(sum1 - sum2)

if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    n = int(input())

    a = []

    for _ in range(n):
        a.append(list(map(int, input().rstrip().split())))

    result = diagonalDifference(a)

    f.write(str(result) + '\n')

    f.close()
