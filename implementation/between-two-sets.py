#https://www.hackerrank.com/challenges/between-two-sets/problem

# You will be given two arrays of integers. You will be asked to determine all integers that satisfy the following two conditions:

# 1. The elements of the first array are all factors of the integer being considered
# 2. The integer being considered is a factor of all elements of the second array
# These numbers are referred to as being between the two arrays. You must determine how many such numbers exist.

#!/bin/python3

import os
import sys
from functools import reduce
from fractions import gcd

# https://www.mathblog.dk/hackerrank-between-two-sets-in-python/
#
# Complete the getTotalX function below.
#

def gcd(a, b):
    while a % b != 0:
        a, b = b, (a % b)
    return b

def lcm(a, b):
    return a * b // gcd(a, b)


def getTotalX(a, b):
    min_gcd = reduce(gcd, b)
    max_lcm = reduce(lcm, a)
    count = sum([1 for x in range(max_lcm, min_gcd + 1, max_lcm) if min_gcd % x == 0])
    return count


if __name__ == '__main__':
    f = open(os.environ['OUTPUT_PATH'], 'w')

    nm = input().split()

    n = int(nm[0])

    m = int(nm[1])

    a = list(map(int, input().rstrip().split()))

    b = list(map(int, input().rstrip().split()))

    total = getTotalX(a, b)

    f.write(str(total) + '\n')

    f.close()