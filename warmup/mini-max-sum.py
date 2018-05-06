#https://www.hackerrank.com/challenges/mini-max-sum/problem

#!/bin/python3

import os
import sys

#
# Complete the miniMaxSum function below.
#
def miniMaxSum(arr):
    ar_total = []
    for i in range(len(arr)):
        ar = [arr[j] for j in range(len(arr)) if i != j]
        ar_total.append(sum(ar))
    print('{} {}'.format(min(ar_total), max(ar_total)))


if __name__ == '__main__':
    arr = list(map(int, input().rstrip().split()))

    miniMaxSum(arr)
